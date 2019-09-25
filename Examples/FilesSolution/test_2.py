
def check_positive(func):

    def inner_func(*args):
        res = func(*args)
        return res

    return inner_func


@check_positive
def sum_total(*args):
    return sum(args)
# print(sum_total(1,2,3,4,54))


def integer_output(func,*args):
    res = func(*args)
    return int(res)

print(integer_output(lambda x,y:x**y,2,3))