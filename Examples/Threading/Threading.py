import threading
import queue
import time



list = []

def func(num,queue):
    time.sleep(2)
    queue.put(num)

q=queue.Queue()


for i in range(10):
    thread = threading.Thread(target=func,args=(i,q))
    list.append(thread)
    thread.start()

#
for th in list:
    th.join()

while not q.empty():
    t=q.get()
    print(t)
