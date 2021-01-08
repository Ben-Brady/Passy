from setuptools import setup

setup(
    name='Passy',
    version='0.0.1',
    description='A in-developement package',
    url="https://github.com/ThatGayKid/Passy",
    author="Ben Brady",
    author_email="benbradybusiness@gmail.com",
    py_modules=["passy"],
    package_dir={'': 'src'},
    install_requires = [
        "pycryptodome~=3.9.9",
    ],
    extras_requires = {
        "dev": [
            "pytest>=6.2.1",
            "check-manifest>=0.46",]
    }
)