import sys
from pathlib import Path
from json import load as jload, dump as jdump, JSONDecodeError
from secrets import compare_digest

import internal.Encrypt as internal

class Database:
    def __init__ (self):
        self.Version  = "0.0.1"
        self.UserDict = {}
    
    def __eq__ (self,other):
        return self.UserDict == other.UserDict
    def __ne__ (self,other):
        return self.UserDict != other.UserDict
    
    def __lt__ (self,other):
        if type(other) == Database:
            return len(self.UserDict) < len(other.UserDict)
        else:
            return len(self.UserDict) < other
    def __le__ (self,other):
        if type(other) == Database:
            return len(self.UserDict) <= len(other.UserDict)
        else:
            return len(self.UserDict) <= other
    def __gt__ (self,other):
        if type(other) == Database:
            return len(self.UserDict) > len(other.UserDict)
        else:
            return len(self.UserDict) > other
    def __ge__ (self,other):
        if type(other) == Database:
            return len(self.UserDict) >= len(other.UserDict)
        else:
            return len(self.UserDict) >= other
    
    def __len__ (self):
        return (len(self.UserDict))
    
    def check(self,Username,Password):
        """
        Checks a set of credentials to if they're valid.
        Returns a bool representing success.
        """
        return internal.Check[self.Version](Username,Password,self.UserDict)

    def add(self,Username,Password,**kwargs):
        """
        Adds a user to the database with the username and password properties.
        Note: The Attibutes propery is the kwargs arguments
        """
        Key,Entry = internal.Encrypt[self.Version](Username,Password)
        #If the account already exists in the User Dictionary
        if Key in self.UserDict:
            return False
        #If there are kwargs
        if bool(kwargs):
            Entry.append(kwargs)
        #Adds the entry to the internal dictionary
        self.UserDict[Key] = Entry
        #Return Success
        return True
    
    
    def load(self,File):
        #if File isn't a path object
        if type(File) != type(Path()): raise TypeError ("Non-pathlib.path object used")
        #If file doesn't exist, riase a FileNotFoundError
        if File.exists() == False: raise FileNotFoundError
        
        with open(File, 'r') as f:
            self.UserDict = jload(f)

    def save(self,File):
        #if File isn't a path object
        if type(File) != type(Path()): raise TypeError ("Non-pathlib.path object used")
        
        with open(File, 'w') as f:
            jdump(self.UserDict, f)