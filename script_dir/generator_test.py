'''测试 生成器'''
def fun():
    print('starting generator')
    value = yield 10
    print(value)

f = fun()
print(f.send(None))
# print(next(f))
try:
    print(f.send('welcome'))
except StopIteration:
    print('endind')

