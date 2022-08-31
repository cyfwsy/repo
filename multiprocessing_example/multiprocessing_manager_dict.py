import multiprocessing
import pprint

def worker(d,key,value):
    d[key] = value

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    d = manager.dict()
    jobs = [
        multiprocessing.Process(
            target=worker,
            args=(d,i,i*2)
        )
        for i in range(10)
    ]
    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()
        
    # pp = pprint.PrettyPrinter()
    # pp.pprint(d)
    print('Result:',d)