import os
from passy import Database
from pathlib import Path
test1=Database()
os.remove(Path(Path.cwd(),r'test/Test_Data/test1.json'))
os.remove(Path(Path.cwd(),r'test/Test_Data/test2.json'))
test1.add("test1","pass1")
test1.add("test2","pass2")
test1.save(Path(Path.cwd(),r'test/Test_Data/test1.json'))
test1.add("test3","pass3")
test1.save(Path(Path.cwd(),r'test/Test_Data/test2.json'))