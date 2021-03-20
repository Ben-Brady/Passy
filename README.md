# Install

| The easiest way to install passy is to use python's pip module
|
| Use this command in your terminal

Using pip::

    pip install passy
    or
    python -m pip install passy

| If you get an error use the documentation to reinstall your `pip`_

.. _pip: https://pip.pypa.io/en/stable/installing/



# Specification

## Scope

This project is intended to be a credential handler for python, to allow developers to not have to createa their own implemntations and instead can use an existing implemntation that is resistant to side channel attacks.
Future additions such as built in 2-factor autherntication methods may be enabled.


## Security

The internal database,stored in the class object, consists of the a python dictionary which stores:

- The Username Hash
- The Password Hash
- The Password Salt
- User Provided Kwargs
- An Entrytion Verison Number

Stored in this format::

    Databse.UserDict={
    UsernameHash:[
        PasswordHash,
        PasswordSalt,
        kwargs,
        VersionNumber]
    }

- Each username is hashed with SHA256 to prevent account association
- Each password is hashed with SHA256 and a salt is applied through the built-in python secrets.token_bytes function *
- The additional kwargs are stored in plain text dictionary
- The Version number is stored as a plain text string for account migration and recovery

Note: This will be changed to argon2 in future versions

## Migration and Recovery

With each entry in the user dictionary a version number is stored alongisde. This version number is used to update outdated entries to more modern format when unlocked, this is because inoder for the format transfer to take place the entry needs to be unencrypted so this cannot be done proactively.

The encryption functions to do this are stored in internal.Encrypt


# Database



## Supported Methods



### == / !=

Checks if two databases are equal.

## < / <= / > / >=

Compares the length of two database objects.

### len 

Returns the total accounts in a database as an int

## Functions

### Save

The "Save" function is used to save the database to a file::

    .save(File)

Outputs the internal user dictionary to a json file stored at the File parameter

#### Arguments

    File (pathlib.Path)
        Specifies a file path where the user dictionary with be saved to

#### Errors

TypeError: If the File argument isn't a pathlib.Path object

#### Examples

    Saves to the provided Path object::

        import pathlib
        Foo = pathlib.Path("C:","Bar","Users.json")
        Database.Save(ExamplePath)

### Load

The "Load" function is used to load the database from a json file::

    Database.load(File)


#### Arguments

    File (pathlib.Path)
        Specifies a custom file path to load the internal dictionary


#### Errors

- TypeError : if the File argument isn't a pathlib.Path object
- FileNotFoundError: if the targetted File doesn't exist.

#### Examples

    Load from the provided Path object:

        import pathlib
        ExamplePath = pathlib.Path("D:","Example","Users.json")
        database.Load(ExamplePath)

### Add Account

Adds a new accounts to the database::


    .add(Username,Password,[Attributes])

| Adds an entry with the specified credentials and an optional attributes folder stored along with it
Returns a bool to represent success:

    - True,  if the entry was successfully added
    - False, if there is already a user with that name

#### Arguments

    Username (string)
        Specifies the created username for entry

    Password (string)
        Specifies the created user's password

    **kwargs
        Any kwargs will be stored alongside the user's entry

--------
Examples
--------
    
    Adding an account with the name "TestUser"

        Database.add('TestUser','password')
        
        Output: True

    Adding an account with kwargs

        Database.add('user','pass',Example=True)
        
        Output: True

    Adding a duplicate user

        Database.add('Sameuser','dsfhfns')
        Output: True

        Database.add('Sameuser','sdfasdg')
        Output: False
        


## Check Credentials

Checks if a set of credentials have a valid owner

    Database.check(Username,Password)

Returns a bool to check if login was valid

#### Arguments

    Username (string)
        Specifies the login username

    Password (string)
        Specifies the login password

#### Examples
    
    Checking credentials for a valid user::
        
        Database.check('RealUser','password')

        Output: True

    Checking credentials for an invalid user::

        Database.check('BadUser','password')

        Output: False
