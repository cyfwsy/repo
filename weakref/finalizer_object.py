import weakref
class Object:
    pass

# kenny = Object()
# weakref.finalize(kenny, print, "You killed Kenny!")  
# del kenny

# def callback(x, y, z):
#     print("CALLBACK")
#     return x + y + z

# obj = Object()
# f = weakref.finalize(obj, callback, 1, 2, z=3)
# print(f.alive)
# if f() == 6:
#     print('callback result is 6')
# print(f.alive) 
# f()                     # callback not called because finalizer dead
# del obj                 # callback not called because finalizer dead

obj = Object()
weakref.finalize(obj, print, "obj dead or exiting")
exit()