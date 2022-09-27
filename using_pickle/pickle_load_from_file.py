import pickle
import sys
from pickle_dump_to_file import SimpleObject

filename = sys.argv[1]
with open(filename,'rb') as in_s:
    while True:
        try:
            obj = pickle.load(in_s)
        except EOFError:
            break
        else:
            print('READ >>> {} ({})'.format(obj.name,obj.name_backwards))