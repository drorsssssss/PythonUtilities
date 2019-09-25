import random
import threading
from queue import Queue

global_path="/Users/dsivan/GitRepos/PythonUtilities/Examples/PubSub/"


def consume(filename,queue):
    while True:
        val=queue.get()
        with open(f"{global_path}/{filename}.txt","a") as file_obj:
            file_obj.write(val+'\n')
        queue.task_done()


def dispatcher(**kwargs):
    while True:
        val = kwargs["main"].get()
        target_queue = kwargs[val]
        target_queue.put(val)
        kwargs["main"].task_done()


def publisher(queue,n=5):
    for _ in range(n):
        choices = ['a','b','c']
        choiced = random.choice(choices)
        queue.put(choiced)


def main():
    print('Start')

    main_q = Queue()

    q_a=Queue()
    q_b=Queue()
    q_c=Queue()

    dict_queues = {"a":q_a,"b":q_b,"c":q_c,"main":main_q}

    #Create 3 subscriber threads
    thrd_a = threading.Thread(target=consume,args=("tasks_a",q_a))
    thrd_a.daemon=True
    thrd_a.start()

    thrd_b = threading.Thread(target=consume,args=("tasks_b",q_b))
    thrd_b.daemon=True
    thrd_b.start()

    thrd_c = threading.Thread(target=consume,args=("tasks_c",q_c))
    thrd_c.daemon=True
    thrd_c.start()


    #Create 3 dispatcher threads
    for _ in range(3):
        thrd = threading.Thread(target=dispatcher,kwargs=(dict_queues))
        thrd.daemon=True
        thrd.start()


    #Create 3 publisher threads
    for _ in range(3):
        thrd = threading.Thread(target=publisher,args=(main_q,))
        thrd.daemon=True
        thrd.start()

    for v in dict_queues.values():
        v.join()
    print('End')

main()