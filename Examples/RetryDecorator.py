

def Retry(func):

    def inner(a):
        res = func(a)
        return res

    return inner



@Retry
def stam(z):
    print("dror")
    return z*2

print(stam(2))
