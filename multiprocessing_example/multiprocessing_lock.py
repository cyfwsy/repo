import multiprocessing

def worker_with(lock,l):
    with lock:
        l.append('worker_with data is appended')
        print('worker_with data',l,id(l))
        
def worker_no_with(lock,l):
    lock.acquire()
    try:
        l.append('worker_no_with data is appended')
        print('worker_no_with data',l,id(l))
    finally:
        lock.release()
        
        
if __name__ == '__main__':        
    manager = multiprocessing.Manager()
    l = manager.list(['main data'])
    lock = multiprocessing.Lock()
    w1 = multiprocessing.Process(target=worker_with,args=(lock,l))
    w2 = multiprocessing.Process(target=worker_no_with,args=(lock,l))
    w1.start()    
    w2.start()   

    w1.join() 
    w2.join()
    print('main module',l,id(l))
