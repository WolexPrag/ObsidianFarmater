import os
import pathlib
from FileDataManager import *

def test_FileDataManager():
    fileManager = FileDataManager(Path(os.getcwd()))
    fileManager.Open(Path('/Container'))
    print( fileManager.pathFile)
    assert True