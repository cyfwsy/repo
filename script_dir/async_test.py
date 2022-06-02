"生成器做为协程"
from collections import deque

def countdown(n):
    while n > 0:
        print('T-minus',n)
        yield
        n -= 1
    print('Blastoff')

def countup(n):
    x = 0
    while x < n:
        print('counting up',x)
        yield
        x += 1

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self,task):
        "装入一个新任务"
        self._task_queue.append(task)

    def run(self):
        "运行队列中的任务"
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                #运行下一个 yield 语句
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass


#示例
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()



