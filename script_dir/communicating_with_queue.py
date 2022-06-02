'''进程间使用队列进行通讯'''
import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0,256)
            self.queue.put(item)
            print('Process Producer:item {} appended to queue by {}'.format(item,self.name))
            time.sleep(1)
            # print('The size of queue is {}'.format(self.queue.qsize()))

class consumer(multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print('the queue is empty')
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Process Consumer:item {} popped from queue by {}'.format(item,self.name))
                time.sleep(1)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p = producer(queue)
    c = consumer(queue)
    p.start()
    c.start()
    p.join()
    c.join()