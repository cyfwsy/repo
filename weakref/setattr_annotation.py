class Example:
    def __init__(self,name='fix_name',**annotation):
        self._name = name
        for k,v in annotation.items():
            setattr(self,k,v)
            
ex = Example('my_name',a=1,b=2)
print(ex.__dict__)
print(ex.a)
print(ex.b)