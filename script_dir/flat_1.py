'''扁平化迭代'''
from collections.abc import Iterable

def flatten(items,ignore_types = (str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

# items = [1,2,[2,6,[3,4,7,9,23,45],345],99,45]
# for i in flatten(items):
#     print(i)

items1 = ['Dave','Paula',['Thomas','Lewis'],'Anderson',{'Ivan':9,'Tom':0}]
for i in flatten(items1):
    print(i)