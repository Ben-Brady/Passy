#######
Classes
#######

........
Database
........

=======
Methods
=======

=====
.Save
=====

The "Save" function is used to save the database to a file::

    .Save(File)

Outputs the internal user dictionary to a json file stored at the File parameter

---------
Arguments
---------

    File (pathlib.Path)
        Specifies a file path where the user dictionary with be saved to

------
Errors
------

- TypeError : if the File argument isn't a pathlib.Path object

--------
Examples
--------

    Saves to the provided Path object::

        import pathlib
        ExamplePath = pathlib.Path("D:","Users","Users.json")
        Database.Save(ExamplePath)

|
|

====
Load
====

The "Load" function is used to load the database from a json file::

    .Load(File)


---------
Arguments
---------

- File (pathlib.Path)
    | Specifies a custom file path to load the internal dictionary


------
Errors
------

- TypeError : if the File argument isn't a pathlib.Path object
- FileNotFoundError: if the targetted File doesn't exist.

--------
Examples
--------

    Load from the provided Path object::

        import pathlib
        ExamplePath = pathlib.Path("D:","Users","Users.json")
        database.Load(ExamplePath)

|

==============
Add Account
==============

Adds a new accounts to the internal user dictionary::


    Add(Username,Password,[Attributes])

Adds a new entry to the internal user dictionary

---------
Arguments
---------

    Username (string)
        Specifies the created username for entry

    Password (string)
        Specifies the created user's password

Optional
========

    Atributes (dict)
        Stores a secure dictionaray associated with the user

| Returns a bool to represent a sucessfully added user
| Please refer to the specification's section on account storage for security info

--------
Examples
--------
    
    Adding account with the name "TestUser"::

        impoty passy
        passy.Add('TestUser','password')
        
        Output: True

|
|

=================
Check Credentials
=================


Adds a new accounts to the internal user dictionary::

    Check(Username,Password)

Returns a bool to check if login was valid

---------
Arguments
---------

    Username (string)
        Specifies the login username

    Password (string)
        Specifies the login password

--------
Examples
--------
    
    Checking credentials for "TestUser"::

        import passy
        passy.Check('TestUser','password')

        Output: True