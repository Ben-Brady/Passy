"""""""""""""""""""
Passy Specification
"""""""""""""""""""

.....
Scope
.....

| This project is intended to be a credential handler for python, to allow
| developers to not have to createa their own implemntations and instead
| can use an existing implemntation that is resistant to side channel attacks.
| Future additions such as built in 2-factor autherntication methods may be enabled.

........
Security
........

The internal database,stored in the class object, consists of the a python dictionary which stores:

- The Username Hash
- The Password Hash
- The Password Salt
- A User Provided Dictionary
- A Version Number for Migration and Recovery

Stored in this format::

    Databse.UserDict={
    UsernameHash:[
        PasswordHash,
        PasswordSalt,
        kwargs,
        VersionNumber]
    }

* Each username is hashed with SHA256 to prevent account association
* Each password is hashed with SHA256 and a salt is applied through the built-in python secrets.token_bytes function *
* The additional kwargs are stored in plain text dictionary
* The Version number is stored as a plain text string 

| \* - This will be changed to argon2 in future versions
......................
Migration and Recovery
......................

| With each entry in the user dictionary a version number is stored alongisde.
| This version number is used to update outdated entries to more modern format when unlocked,
| this is because inoder for the format transfer to take place the entry needs to be unencrypted
| so this cannot be done proactively.
|
| The encryption functions to do this are stored in internal.Encryption