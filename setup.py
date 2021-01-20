from setuptools import setup

setup(
    name='passy',
    version='0.0.1',
    description='A credential handler for python',
    url="https://github.com/ThatGayKid/Passy",
    author="Ben Brady",
    author_email="benbradybusiness@gmail.com",
    py_modules=["passy"],
    package_dir={'': 'src'},
    install_requires = [],
    extras_requires = {
        "dev": [
            "pytest>=6.2.1",
            ]
    }
)