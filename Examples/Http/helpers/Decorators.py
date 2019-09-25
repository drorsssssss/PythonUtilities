import time

def func_duration(func):
    """ This decorator will calculate the total duration for the func execution"""

    def inner(*args):
        start_time=time.time()
        res = func(*args)
        duration=round(time.time()-start_time,2)
        print(f'The function run: {duration} sec')
        return res
    return inner