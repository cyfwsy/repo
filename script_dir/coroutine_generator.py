"协程测试"
import time
def coroutine():
    print('开始协程测试')
    result = None
    while True:
        recv = yield result
        if recv == 'END':
            break
        else:
            result = (time.time(),recv)
    print('协程结束')

f = coroutine()
print(f)
next(f)
data = [12,34,67,98,11,90,45,34,54,'END']
for value in data:
    try:
        res = f.send(value)
        print(res)
    except StopIteration:
        print('协程结束')