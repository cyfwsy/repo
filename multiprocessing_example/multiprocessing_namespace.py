import multiprocessing
import time

def producer(ns,event):
    ns.value = 'This is a value'
    time.sleep(1)
    event.set()
    
def consumer(ns,event):
    try:
        print('Before event : {}'.format(ns.value))
    except Exception as err:
        print('Before event error'.format(str(err)))
    event.wait()
    print('After event : {}'.format(ns.value))
    
if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    ns = mgr.Namespace()
    event = multiprocessing.Event()
    
    p = multiprocessing.Process(target=producer,args=(ns,event))
    c = multiprocessing.Process(target=consumer,args=(ns,event))
    
    c.start()
    p.start()
    
    c.join()
    p.join()