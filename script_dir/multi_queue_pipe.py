'''用多队列实现管道，多个任务执行不同阶段的工作'''
from queue import Queue
from threading import Thread

class ClosableQueue(Queue):
    SENTINEL = object()
    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # Cause the thread to exit
                yield item
            finally:
                self.task_done()

class StoppableWorker(Thread):
    def __init__(self,func,in_queue,out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

#指定多个任务
def download(item):
    return item
def resize(item):
    return item
def upload(item):
    return item
# if __name__ == '__main__':
# #实例化管道中的各个队列
#         download_queue = ClosableQueue()
#         resize_queue = ClosableQueue()
#         upload_queue = ClosableQueue()
#         done_queue = ClosableQueue()
#
#         #实例化线程
#         threads = [
#             StoppableWorker(download,download_queue,resize_queue),
#             StoppableWorker(resize,resize_queue,upload_queue),
#             StoppableWorker(upload,upload_queue,done_queue),
#         ]
#         for thread in threads:
#             thread.start()
#
#         for _ in range(1000):
#             download_queue.put([3,6])
#         download_queue.close()
#         download_queue.join()
#         resize_queue.close()
#         resize_queue.join()
#         upload_queue.close()
#         upload_queue.join()
#         print(done_queue.qsize(),'items finished')
#         done_queue.close()
#
#         for item in done_queue:
#             print(item)
#         done_queue.join()
#         for thread in threads:
#             thread.join()


# 每个阶段可使用多个任务处理这个阶段的同一个队列
if __name__ == '__main__':

    def start_threads(count,*args):
        threads = [StoppableWorker(*args) for _ in range(count)]
        for thread in threads:
            thread.start()
        return threads
    def stop_threads(closable_queue,threads):
        for _ in threads:
            closable_queue.close()
        closable_queue.join()
        for thread in threads:
            thread.join()

    download_queue = ClosableQueue()
    resize_queue = ClosableQueue()
    upload_queue = ClosableQueue()
    done_queue = ClosableQueue()

    download_threads = start_threads(3,download,download_queue,resize_queue)
    resize_threads = start_threads(2,resize,resize_queue,upload_queue)
    upload_threads = start_threads(2,upload,upload_queue,done_queue)

    for _ in range(10):
        download_queue.put([2,4,5,6,7])

    stop_threads(download_queue,download_threads)
    stop_threads(resize_queue,resize_threads)
    stop_threads(upload_queue,upload_threads)

    print(done_queue.qsize(),'items finished')
    done_queue.close() # 保证退出done_queue 的迭代
    for item in done_queue:
            print(item)
    done_queue.join() # 保证退出done_queue 的迭代



