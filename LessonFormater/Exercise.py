
class Exercise:
    number:int
    text:str
    def __init__(self,text:str,number:int):
        self.text = text;
        self.number = number;
        pass
    def __str__(self):
        return f"{self.number}. {self.text}"
    pass
