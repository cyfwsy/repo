"To see how property() is implemented in terms of \
    the descriptor protocol, here is a pure Python equivalent:"
class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
        self._name = ''

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError(f'unreadable attribute {self._name}')
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError(f"can't set attribute {self._name}")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError(f"can't delete attribute {self._name}")
        self.fdel(obj)

    def getter(self, fget):
        prop = type(self)(fget, self.fset, self.fdel, self.__doc__)
        prop._name = self._name
        return prop

    def setter(self, fset):
        prop = type(self)(self.fget, fset, self.fdel, self.__doc__)
        prop._name = self._name
        return prop

    def deleter(self, fdel):
        prop = type(self)(self.fget, self.fset, fdel, self.__doc__)
        prop._name = self._name
        return prop
    
class C:
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    # x = Property(getx, setx, delx, "I'm the 'x' property.")
    
    @Property
    def valuex(self):
        return self._x
    
    @valuex.setter
    def valuex(self,value):
        self._x = value
        
    @valuex.deleter
    def valuex(self):
        del self._x
        
        
    
    
# c = C()
# c.x = 80
# print(c.x)
# c.x = 100
# print(vars(c))

c = C()
c.valuex = 100
print(c.valuex)
c.valuex = 10000
print(c.valuex)
print(vars(C))
print(vars(c))