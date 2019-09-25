from time import sleep

def Retry(n,sec):
    def decorator(func):
        def wrapper(*args,**kwargs):
            exception=None
            for i in range(1,n+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"Retry number {i}, Exception Msg: {e}")
                    sleep(sec)
                    exception=e

            raise exception
        return wrapper
    return decorator






