"""""""""""""""""""
Passy Specification
"""""""""""""""""""

.....
Scope
.....

| The projects scope only consists of organising secure login sessions
|
| The project is made for developers to not worry about the ins and outso f storing passwords and operating login sessions.
| The program will operate as a black box in which the user provides instructions and receives output, this helps to prevent
| to protect the developers from exposing themselves.
|
| The program isn't designed to handle features such as autosaving and backups of the user dictionary, this is down to the
| developer's implementation of the package, it's their responsibility for that.
|
| If there are 


........
Security
........

The internal databse consists of the a python dictionary which stores:

- The Username Hash
- The Password Hash
- The Password Salt
- A User Provided Data Structure
- A Version Number for Migration

Stored in this format::

    UserDict={
    UsernameHash:[
        PasswordHash,
        PasswordSalt,
        Attributes,
        VersionNumber]
    }


- Each username is hashed with SHA512 to prevent account association
- Each password is hashed with SHA256 and a salt is applied through the built-in python secrets.token_bytes function
- The attributes dictioanry is plain texxtas of current version(Will be changed in future versions)

......................
Migration and Recovery
......................

| With each entry in the user dictionary a version number is stored.
| This version number is used to update outdated entries to more modern format
| The functions to do this are stored in internal.AccountMigration