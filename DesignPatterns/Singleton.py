


class OneOnly:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(OneOnly)
        return cls.singleton

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


x= OneOnly('dror')
z=OneOnly('soso')
x.print_name()
z.print_name()
