from queue import Queue
from Examples.Http.helpers import Functions
import random
import threading
import time


def publish(queue,symbols):
    """ Publish random symbol to Queue"""

    while True:
        symbol = random.choice(symbols)
        queue.put(symbol)


def subscribe(queue):
    """ Subscribe to Queue and perform http request for symbol"""

    while True:
        element = queue.get()
        with open("/Users/dsivan/GitRepos/PythonUtilities/Examples/Http/output.txt","a") as output_file:
            output_file.write(element+"\n")
        queue.task_done()


def main():

    print("Start")

    url="https://financialmodelingprep.com/api/v3/stock/real-time-price/"
    symbols = ["ADBE","CRM","GOOG","AAPL","DCO"]
    q = Queue()



    # Run 1 thread for subscribing and write to file
    thr = threading.Thread(target=subscribe,args=(q,))
    thr.daemon=True
    thr.start()


    # Run publish actions to Queue
    threads=[]
    for i in range(5):
        thr = threading.Thread(target=publish,args=(q,symbols))
        thr.daemon=True
        threads.append(thr)
        thr.start()


    q.join()


    print("this program ran async file writing")




main()
