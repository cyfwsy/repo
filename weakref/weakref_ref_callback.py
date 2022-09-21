import weakref
class ExtensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))
        
def callback(reference):
    # invoked when referenced object deleted
    print('callback({!r})'.format(reference))
obj = ExtensiveObject()
r = weakref.ref(obj,callback)
print('obj:',obj)
print('ref:',r)
print('r():',r())

print('Deleting obj:')
del obj
print('r()',r())