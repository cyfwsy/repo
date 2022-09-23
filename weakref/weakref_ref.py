import weakref
class ExtensiveObject:
    def __init__(self):
        self._data = 0
        
    def __del__(self):
        print('(Deleting {})'.format(self))
    
obj = ExtensiveObject()
r = weakref.ref(obj)
print('obj:',obj)
print('ref:',r)
print('r():',r())

print('Deleting obj:')
del obj
print('r()',r())
    