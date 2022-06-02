'''生成器的实例'''
# 做一个装饰器
import time

def coroutine(func):
    def wrapper(*args,**kvargs):
        g = func(*args,**kvargs)
        next(g)
        return g
    return wrapper


@coroutine
def countdown(n):
    print('coroutine')
    result = None
    i = 1
    while n >= 0:
        data = yield result
        print('第 {} 次 接收外部数据'.format(i))
        print('接收的数据是{!r}'.format(data))
        i += 1
        n -= 1
        result = (time.time(), data)
print('结束 countdown')
n = 5
g = countdown(n)


for j in range(10):
    try:
        print('外部接收的生成器处理的数据 {}'.format(g.send(j)))
    except StopIteration:
        print('结束生成器')
