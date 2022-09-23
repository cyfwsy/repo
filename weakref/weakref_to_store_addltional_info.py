import weakref

class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None,/, **annotation):
        super().__init__(ob, callback)
        self._counter = 0
        for k, v in annotation.items():
            setattr(self,k,v)
            

    def __call__(self):
        """Return a pair containing the referent and the number of
        times the reference has been called.
        """
        ob = super().__call__()
        if ob is not None:
            self._counter += 1
            ob = (ob, self._counter)
        return ob
    
class ExampleObj:
    def __init__(self,name):
        self.name = name
    def do_something(self):
        print('instance ({})'.format(self.name))
        
obj = ExampleObj('Myname')
obj_ref = ExtendedRef(obj,a=1,b=2)
print(obj_ref.__dict__)
print('obj>>>',obj)
print('obj_ref>>>',obj_ref)
# print('obj_ref()>>>',obj_ref())
# print('obj_ref()>>>',obj_ref())
print(obj_ref.a,obj_ref.b)
obj_ref.a = 'abcd'
print(obj_ref.a)
# print(obj_ref()[0].do_something())
