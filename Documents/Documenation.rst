"""""""""""""
Documentation
"""""""""""""

.............
Specification
.............

All usernames are saved as a sha-512 hash with a salt generated from their name

.........
Functions
.........

====
Save
====

The "Save" function is used to save the internal user dictionary to a file::

    Save(,[FileName[,FilePath]])


Outputs the internal user dictionary to a json file and returns a bool to represent if it sucessfully saved

---------
Arguments
---------

Optional
========

- FileName (String)
    | Specifies a custom file name where the output will be stored
    | Defaults to 'credentials.json'

- FilePath (String,Path)
    | Specifies a custom file path where the output will be stored
    | Defaults: current working directory

--------
Examples
--------
    Saving to Users.json::

        Save("Users.json")

    Saves to the D:/Users directory with the name Users.json::

        Save('Users.json','D:Users')

    Saves to the provided Path object::

        from pathlib import Path
        ExamplePath = Path("D:","Users")
        Save('Users.json',Example_Path)

==============
Add Account
==============

Adds a new accounts to the internal user dictionary::

    Add(Username,Password,[Attributes])

Adds a new entry to the internal user dictionary

---------
Arguments
---------

Username (String)
    Specifies the created username for entry

Password (String)
    Specifies the created user's password

Atributes (Any)
    Stores a data strucuture next

Returns a bool to represent a sucessfully added user
Please refer to the specification's section on account storage for security info

--------
Examples
--------
    
    Adding account with the name "TestUser"::

        Add('TestUser','password')

-----------------
Check Credentials
-----------------

Adds a new accounts to the internal user dictionary::

    Check(Username,Password)

Returns a bool to check if accounts is valid
