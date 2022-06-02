"测试协程函数"
def corou():
    result = []
    while True:
        data = yield result
        if data == "quit":
            print('退出协程')
            break
        print(data)
        result.append(data)

def main():
    g = corou()
    result = g.send(None)
    for i in range(20):
        try:
            result = g.send(i)
            print(result)
        except StopIteration:
            break
    try:
        g.send('quit')
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
