import weakref
class ExtensiveObject:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print('Deleting ({})'.format(self))
        
obj = ExtensiveObject('MyObject')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('Via : obj',obj.name)
print('Via : ref',r().name)
print('Via : proxy',p.name)
del obj
print('Via : proxy',p.name)