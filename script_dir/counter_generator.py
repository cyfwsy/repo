def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1
            
g = counter(10)
print(g)
# print(next(g))
# print(next(g))
print(g.send(None))
print(g.send(8))
print(g.send(None))
print(g.send(None))
print(next(g))
print(next(g))
print(g.__next__())