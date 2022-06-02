'''内联函数回调'''
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

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func,a.args,callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

def add(x,y):
    return x + y
def mul(x,y):
    return x * y

@inlined_async
def main_task():
    r = yield Async(add,(2,3))
    print(r)
    r = yield Async(add,('hello','world'))
    print(r)
    r = yield Async(mul,(99,99))
    print(r)
    for n in range(10):
        r = yield Async(mul,(n,n+1))
        print(r,end=',')
    print('Goodbye')
# main 任务可以任意设定
main_task()