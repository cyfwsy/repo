def apply_async(func,args,*,callback):
    #compute the result
    result = func(*args)
    #invoke the callback with result
    callback(result)

from queue import Queue
from functools import wraps

class Async:
    def __init__(self,func,args):
        self.func = func
        self.args = args

def schedule_coroutine(g):
        f = generator_coroutine()
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func,a.args,callback=result_queue.put)
            except StopIteration:
                break

def add(x,y):
    return x + y
def mul(x,y):
    return x * y

def generator_coroutine():
    r = yield Async(add,(2,3))
    print(r)
    r = yield Async(add,('hello','world'))
    print(r)
    r = yield Async(mul,(99,99))
    print(r)
    r = yield Async(mul,(100,100))
    print(r)
    for n in range(10):
        r = yield Async(mul,(n,100))
        print(r,end=',')
    print('/n')
    print('Goodbye')
# 調度執行協程任務， 任务可以任意设定
schedule_coroutine(generator_coroutine())