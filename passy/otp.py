import json
import pyotp
from typing_extensions import Self

class OTP:
    totp: pyotp.TOTP
    secret: str
    backup_codes: list[str]


    def __init__(self, secret: str, backup_codes: list[str]):
        self.secret = secret
        self.backup_codes = backup_codes
        self.totp = pyotp.TOTP(self.secret)


    @classmethod
    def create(cls) -> Self:
        secret = pyotp.random_base32()
        backup_codes = [
            pyotp.random_base32(length=8)
            for _ in range(12)
        ]
        return cls(
            secret=secret,
            backup_codes=backup_codes,
        )

    def verify(self, code: str) -> bool:
        return self.totp.verify(code)

    def url(self, *,
            issuer: str|None = None,
            name: str|None = None,
            image_url: str|None = None,
            ) -> str:
        return self.totp.provisioning_uri(
            name=name,
            issuer_name=issuer,
            image=image_url
        )


    def use_backup_code(self, code: str) -> bool:
        if code in self.backup_codes:
            self.backup_codes.remove(code)
            return True
        return False


    @staticmethod
    def loads(data: str) -> Self:
        values = json.loads(data)
        return OTP(
            secret=values["secret"],
            backup_codes=values["backup_codes"],
        )


    def dumps(self) -> str:
        return json.dumps({
            "secret": self.secret,
            "backup_codes": self.backup_codes,
        })
