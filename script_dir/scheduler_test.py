"测试一个任务调度方法,微型操作系统"
from  collections import deque

class ActorScheduler():
    def __init__(self):
        self._actors = {} # name mapping to actor
        self._msg_queue = deque() #message queue

    def new_actor(self,name,actor):
        self._actors[name] = actor
        self._msg_queue.append((actor,None))

    def msg_to_actor(self,name,msg):
        '''binding msg to a actor'''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))
    def run(self):
        '''执行队列中的任务'''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg) #消息送给协程，激活生成器，actor 都是协程
            except StopIteration:
                pass

# 主程序实例
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got',msg)

    def counter(sched):
        while True:
            n = yield #接收协程外的一个msg
            if n == 0:
                break
            # print('绑定msg{}到 printer'.format(n))
            sched.msg_to_actor('printer',n)
            # print('绑定msg{}到 counter'.format(n-1))
            sched.msg_to_actor('counter',n-1) # 递归，但是通过队列，这个协程还负责准备就绪队列

sched = ActorScheduler()
sched.new_actor('printer',printer()) #先注册新的actor，并且构造出协程对象
sched.new_actor('counter',counter(sched))

sched.msg_to_actor('counter',10000) #绑定初始化协程任务
sched.run()

