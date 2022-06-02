from queue import Queue
from threading import Thread
import time


def producer(q):
    runing = True
    while runing:
        for data in range(5):
            print('producing {}.'.format(data))
            q.put(data)
            time.sleep(2)
        print('ending produce')
        q.put(None)
        runing = False


def consumer(q):
    while True:
        data = q.get()
        if data == None:
            break
        print('comsuming {}'.format(data))
        time.sleep(1)
        q.task_done()


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()
q.join()
t1.join()
t2.join()
print('ended ended ended')
