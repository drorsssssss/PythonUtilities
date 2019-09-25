
import time

def time_duration(func):

    def inner():
        begin = time.time()
        func()
        end = time.time()
        print(f"The time duartion: {end-begin}")
    return inner


@time_duration
def tryy():
    print("some function")
    time.sleep(2)


tryy()
