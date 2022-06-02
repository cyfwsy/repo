"反向迭代，生成器"
class countdown:
    def __init__(self,N):
        self.n = N

    def __iter__(self):
        i= self.n
        while i  > 0:
            yield i
            i -= 1

    def __reversed__(self):
        i = 1
        while i <= self.n:
            yield i
            i += 1

count = countdown(10)
for c in count:
    print(c,end=',')
print()
for c in reversed(count):
    print(c,end = ',')