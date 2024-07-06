from pathlib import Path


class FileDataManager:
    pathFolder: Path
    pathFile: Path

    def __init__(self, pathFolder: Path):
        self.pathFolder = pathFolder
        self.pathFile = Path('')
        pass

    def getPath(self):
        return self.pathFolder + self.pathFile

    def CheakPath(self, path: Path):
        return path.exists()

    def CheckPaths(self):
        if (self.CheakPath(self.pathFile) == True):
            return True
        return

    def Select(self, path: Path):
        if (self.CheakPath(self.pathFolder / path) == False):
            return Exception(f"({type(FileDataManager)}):This path was not found")
        pathFile = path
        pass
    def Open(self,path:Path):
        if (self.CheakPath(self.pathFolder /  self.pathFile / path) == False):
            return Exception(f"({type(FileDataManager)}):This path was not found")
        self.pathFile /= path
        pass

    def ReadFile(self):
        file = open(self.getPath())
        output = file.read()
        file.close()
        return file

    pass
