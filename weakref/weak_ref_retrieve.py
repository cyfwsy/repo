import weakref

class List(list): # subclassing
    pass

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid

def id2obj(oid):
    return _id2obj_dict[oid]


obj = List([23,30,100,500,'abcd'])
oid = remember(obj)
print(oid)
print(id2obj(oid))