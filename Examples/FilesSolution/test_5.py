from DesignPatterns.Decorator.RetryDecorator import Retry

class utils:

    @Retry(3,1)
    def util1(self):
        print(1/0)

    def util2(self):
        print(2)


x=utils()
x.util1()
