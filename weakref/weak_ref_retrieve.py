import weakref

class List(list): # subclassing
    pass

class ExamObj:
    def __init__(self,name):
        self._name = name

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]


obj = List([23,30,100,500,'abcd'])
oid = remember(obj)
obj1 = ExamObj('NAME')
oid1 = remember(obj1)

print(oid)
print(id2obj(oid))
print(id2obj(oid1))
print(type(id2obj(oid1)))
print(type(id2obj(oid)))
print(_id2obj_dict)