from setuptools import setup

with open('docs/index.rst','r') as docs:
    long_description=docs.read()

setup(
    name            = 'passy',
    version         = '0.0.2',
    description     = 'A credential handler for python3',
    long_description= long_description,
    url             = "https://github.com/ThatGayKid/Passy",
    author          = "Ben Brady",
    author_email    = "benbradybusiness@gmail.com",
    py_modules      = ["passy","Encrypt"],
    package_dir     = {'':'src'},
    install_requires= [],
    extras_requires = {
        "dev": [
            "pytest>=6.2.1",
            ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ]
)