from unittest import TestCase
from Passy import *

FileName = 'credentials.json'
def test_answer():
    assert (1==2) == True
    
def test_answer():
    assert load(3,2,4234) == True
    
def test_LoadNormal():
    assert CompareFiles(load(FileName)) == True

def test_LoadNonJson():
    assert CompareFiles(load(FileName)) == True
    

def CompareFiles(f):
    try:
        with open(FileName, 'r') as f:
            if f == UserDict:   f.close();return True#If the saved file is identical
            else:               f.close();return False#to the stored one return True
    except FileNotFoundError:#If the file hasn't saved
        return False
    return False#Fallback