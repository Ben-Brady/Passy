"""""""""""""""""""
Passy Specification
"""""""""""""""""""

.....
Scope
.....

|
|
|
|
|

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