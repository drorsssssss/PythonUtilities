import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self,name,dob,country):
        self.name=name
        self.dob=dob
        self.country=country

    @abc.abstractmethod
    def get_age(self):
        pass

    @abc.abstractmethod
    def get_country(self):
        pass


class FireMan(Person):
    def __init__(self,name,dob,country,rank):
        super().__init__(name,dob,country)
        self.rank=rank

    def get_rank(self):
        return self.rank

    def get_age(self):
        return self.dob/100

    def get_country(self):
        return self.country


x= FireMan('dror',3111986,'Israel',10)
# y=Person('mango',5,'Israel')

print(x.get_age())
# print(y.get_country())