import random
import multiprocessing
from multiprocessing import Queue

global_path="/Users/dsivan/GitRepos/PythonUtilities/Examples/PubSub/"


def consume(filename,queue):
    while True:
        val=queue.get()
        if val == 'END':

            break
        with open(f"{global_path}/{filename}.txt","a") as file_obj:
            file_obj.write(val+'\n')




def dispatcher(**kwargs):
    while True:
        val = kwargs["main"].get()

        if val == 'END':

            for k,v in kwargs.items():
                if k != 'main':
                    v.put('END')

            break
        target_queue = kwargs[val]
        target_queue.put(val)




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
    processes=[]

    #Create 3 subscriber threads
    thrd_a = multiprocessing.Process(target=consume,args=("tasks_a",q_a))
    processes.append(thrd_a)
    thrd_a.daemon=True
    thrd_a.start()



    thrd_b = multiprocessing.Process(target=consume,args=("tasks_b",q_b))
    processes.append(thrd_b)
    thrd_b.daemon=True
    thrd_b.start()

    thrd_c = multiprocessing.Process(target=consume,args=("tasks_c",q_c))
    processes.append(thrd_c)
    thrd_c.daemon=True
    thrd_c.start()


    #Create 3 dispatcher threads
    for i in range(3):
        thrd = multiprocessing.Process(target=dispatcher,kwargs=(dict_queues))
        processes.append(thrd)
        thrd.daemon=True
        thrd.start()


    #Create 3 publisher threads
    for _ in range(3):
        thrd = multiprocessing.Process(target=publisher,args=(main_q,))
        processes.append(thrd)
        thrd.daemon=True
        thrd.start()

    main_q.put('END')


    while True:
        print(list(map(lambda x: x.is_alive(),processes)))











    print('End')

main()