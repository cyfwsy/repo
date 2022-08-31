"implement a singleton model"
class Singleton:
    def __new__(cls,*args,**kvargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance
    
class Myclass(Singleton):
    def __init__(self,a) -> None:
        self.a = a
        
a = Myclass('abc')
print(a.a)
b = Myclass('xyz')

print(a.a,b.a)
print(id(a),id(b))