import os
import pathlib
import pytest
from LessonFormater import *
from Container import *
from FileDataManager import *


text = testText
start = GetStart(text)
words = GetDividedText(text[start:])
fileManager = FileDataManager(pathlib.Path(pathToEnglish))
allFolders:list = os.listdir(fileManager.pathFolder)




print(f"==========End({len(text)} symbols)==========")
