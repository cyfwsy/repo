"测试 yield from"
import time
def func():
    result = 'quit'
    while True:
        print('休息1秒')
        time.sleep(1)
        data = yield result
        result = data * data


def main():
    f = func()
    # f.send(None)
    print(f.send(None))
    n = 10
    while n > 0:
        data = f.send(n)
        print(n,data)
        n -= 1



if __name__ == '__main__':
    main()