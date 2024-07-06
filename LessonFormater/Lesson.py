from .Exercise import Exercise
class Lesson:
    __exercises:list
    __number:str
    def add(self, exercise: Exercise):
        self.__exercises += exercise
    def count(self):
        return len(self.__exercises)
    def get(self,index:int):
        return self.__exercises[index]
    def remove(self,value):
        self.__exercises.remove(value)
    def __init__(self,number:str):
        self.__number = number
        pass
    pass
