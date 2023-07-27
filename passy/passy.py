from .otp import OTP
from typing import Any
from typing_extensions import Self
from enum import IntEnum
from passlib.hash import argon2
import json
from base64 import b64encode, b64decode


class OTPNeeded(Exception):
    pass

class Auth:
    _password_hash: str
    _otp: OTP|None = None


    def __init__(self, password_hash: str, otp: OTP|None = None):
        self._password_hash = password_hash
        self._otp = otp


    @classmethod
    def create(cls, password: str) -> Self:
        return cls(
            password_hash=argon2.hash(password)
        )


    def add_2fa(self) -> Self:
        self._otp = OTP.create()
        return self


    def login(self, password: str) -> bool:
        if self._otp:
            raise OTPNeeded()
        return argon2.verify(password, self._password_hash)


    def login_with_otp(self, password: str, otp: str) -> bool:
        success = argon2.verify(password, self._password_hash)
        if self._otp is None:
            raise OTPNeeded()

        return success


    def loads(self, data: str) -> Self:
        decoded = json.loads(b64decode(data))
        password_hash = decoded['password_hash']
        if "otp" in decoded:
            otp = OTP.loads(decoded["otp"])
        else:
            otp = None

        return Auth(password_hash=password_hash, otp=otp)


    def dumps(self) -> str:
        data: dict[str, Any] = {
            "password_hash": self._password_hash,
        }
        if self._otp:
            data["otp"] = data["otp"].dumps()

        json_str = json.dumps(data)
        return b64encode(json_str.encode()).decode()

