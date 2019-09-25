from functools import partial

def calc(x,y,**kwargs):
    if 'a' in kwargs.keys():
        print(kwargs['a'])
    else:
        print(x+y)

x=5
y=6
fn = partial(calc,a=9)
fn(1,1)