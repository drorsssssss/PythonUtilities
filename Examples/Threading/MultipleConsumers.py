from queue import Queue
import threading
from itertools import count



def consumer(queue):
    while True:
        task = queue.get()
        print(f'Thread {threading.get_ident()}, value: {task}')
        queue.task_done()


def producer(queue):
    for i in count(1,1):
        queue.put(i)


def main():
    q=Queue()
    threads=[]

    for th in range(10):
        threadd = threading.Thread(target=consumer,args=(q,))
        threads.append(threadd)
        threadd.daemon=True
        threadd.start()

    producer(q)
    q.join()



main()