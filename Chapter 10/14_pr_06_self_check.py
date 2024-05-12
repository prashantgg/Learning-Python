#Yes the self parameter inside a class can be changed to anything
class Att:
    def __init__(slf, name):
        slf.name = name

obj = Att("Harry")
print (obj.name)

