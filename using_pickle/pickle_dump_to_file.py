import pickle
import sys

class SimpleObject:
    def __init__(self,name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        
if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('preserve'))
    data.append(SimpleObject('last'))
    
    file_name = sys.argv[1]
    with open(file_name,'wb') as out_s:
        for obj in data:
            print('writing >>>{} ({})'.format(obj.name,obj.name_backwards))
            pickle.dump(obj,out_s)