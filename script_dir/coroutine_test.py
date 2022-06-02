"测试协程函数"
def corou(n):
    result = []
    while n >= 0:
        data = yield result
        print(data)
        result.append(data)
        n -= 1

def main():
    g = corou(10)
    result = g.send(None)
    for i in range(20):
        try:
            result = g.send(i)
            print(result)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

