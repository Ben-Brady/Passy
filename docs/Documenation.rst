########
Database
########

..............
Dunder Methods
..............


========
\== / != 
========

| Compare two database objects to see if they're identical

================
 < / <= / > / >=
================

| Compares the length of a database object and a int or another database object

=====
 len 
=====

| Returns the total accounts in a database as an int


.........
Functions
.........

====
Save
====

The "Save" function is used to save the database to a file::

    .save(File)

Outputs the internal user dictionary to a json file stored at the File parameter

---------
Arguments
---------

    File (pathlib.Path)
        Specifies a file path where the user dictionary with be saved to

------
Errors
------

TypeError: If the File argument isn't a pathlib.Path object

--------
Examples
--------

    Saves to the provided Path object::

        import pathlib
        ExamplePath = pathlib.Path("D:","Example","Users.json")
        Database.Save(ExamplePath)

|
|

====
Load
====

The "Load" function is used to load the database from a json file::

    .load(File)


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
        ExamplePath = pathlib.Path("D:","Example","Users.json")
        database.Load(ExamplePath)

|

===========
Add Account
===========

Adds a new accounts to the database::


    .add(Username,Password,[Attributes])

| Adds an entry with the specified credentials and an optional attributes folder stored along with it
Returns a bool to represent success:

    - True,  if the entry was successfully added
    - False, if there is already a user with that name

---------
Arguments
---------

    Username (string)
        Specifies the created username for entry

    Password (string)
        Specifies the created user's password

    **kwargs
        Any kwargs will be stored alongside the user's entry

--------
Examples
--------
    
    Adding an account with the name "TestUser"::

        Database.add('TestUser','password')
        
        Output: True

    Adding an account with kwargs::

        Database.add('user','pass',Example=True)
        
        Output: True

    Adding a duplicate user::

        Database.add('Sameuser','dsfhfns')
        Output: True

        Database.add('Sameuser','sdfasdg')
        Output: False
|
|

=================
Check Credentials
=================


Checks if a set of credentials have a valid owner::

    .check(Username,Password)

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
    
    Checking credentials for a valid user::
        
        Database.check('RealUser','password')

        Output: True

    Checking credentials for an invalid user::

        Database.check('BadUser','password')

        Output: False