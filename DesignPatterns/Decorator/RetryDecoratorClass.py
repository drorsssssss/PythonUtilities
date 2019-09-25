

#
# class RetryDecorator:
#     def __init__(self):


class Decorator:
    def __init__(self, func):
        print('Decorating {}'.format(func.__name__))
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args)

@Decorator
def average(x,y):
    return x/y


print(average(1,2))