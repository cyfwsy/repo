"测试 yield from"
import time


def func():
    result = 0
    while True:
        print('休息1秒')
        time.sleep(1)
        data = yield result
        if data == 'quit':
            break
        result = data * data


def main():
    f = func()
    # f.send(None)
    # print(f.send(None))
    print(next(f))
    while True:
        value = input('input value:')
        if value != 'quit':
            try:
                value = int(value)
            except ValueError:
                continue
                
        try:
            result = f.send(value)
        except StopIteration:
            print('stop coroutine')
            break
        else:
            print(result)
            

if __name__ == '__main__':
    main()
