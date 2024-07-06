def GetStart(text:str):
    output:int = text.find("---")+3
    output += text[output:].find("---")+3
    return output
def GetDividedText(text:str):
    words:list = []
    add = ""
    for chr in text:
        if (chr.isspace() == True):
            words.append(add)
            words.extend(chr)
            add = ""
        else:
            add += chr
        pass