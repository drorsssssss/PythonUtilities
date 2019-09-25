
''' Singleton '''



class singleton:
    _instance=None
    global _name
     _name=None

    def __new__(cls,*args):
        if not cls._instance:
            cls._instance=object.__new__(singleton)
        return cls._instance


    def __init__(self,name):
        if not _name:
            self.name=name


        else:
            self.name=_name




    def printName(self):
        print(self.name)


x1= singleton('dror')
x2= singleton('sivan')

x1.printName()
x2.printName()
