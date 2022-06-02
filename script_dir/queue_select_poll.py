"轮询线程队列"
import queue
import select
import socket
import threading
import random


class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        #create a pair of socket
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(('127.0.0.1',0))
        server.listen(1)
        self._putsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._putsocket.connect(server.getsockname())
        self._getsocket,_ = server.accept()
        server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self,item):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return super().get()

def consumer(queues):
    '''Consumer that reads data on multiple queues simultaneously'''
    while True:
        can_read,_,_ = select.select(queues,[],[])
        for r in can_read:
            item = r.get()
            print('Got:',item)

q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
q4 = PollableQueue()

t = threading.Thread(target=consumer,args=([q1,q2,q3,q4],))
# t.daemon = True
t.start()
# t.join()
queues =[q1,q2,q3,q4]
for i in range(20):
    index = random.randint(0,3)
    queues[index].put(i)
if t.is_alive():
    print('running ')

# q2.put('python')
# q2.put(20)
# q3.put(100)
# q4.put([23,12,90,'quit'])
# while n > 0:
#
#     if t.is_alive():
#         print('thread is running',n)
#     else:
#         print('completed',n)
#     n -= 1

