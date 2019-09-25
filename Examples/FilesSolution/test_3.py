import time
from functools import wraps

def calc_duration(func):
    """A wrapper for calculating time duration"""
    @wraps(func)
    def wrapper(*args):
        """simple"""
        t1=time.time()
        res = func(*args)
        dur = time.time() - t1
        print(f'Time duration: {dur}')

        return res
    return wrapper

@calc_duration
def calculate_something(*args):
    """Heavy calculation"""
    total=0
    for i,v in enumerate(args):
        total+=v**i
    return total


calculate_something(*range(1,5000))
# help(calculate_something)