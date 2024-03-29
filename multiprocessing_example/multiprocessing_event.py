import multiprocessing
import time

def wait_for_event(e):
    "waiting for event to be set before doing anything"
    print('wait_for_event : Starting')
    e.wait()
    print('wait_for_event: e.is_set()->',e.is_set())
    
def wait_for_event_timeout(e,t):
    "wait t seconds and then timeout"
    print('wait_for_event_timeout : Starting')
    e.wait(t)
    print('wait_for_event_timeout e.is_set()->',e.is_set())
    
if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name='block',target=wait_for_event,\
        args=(e,))
    w1.start()
    
    w2 = multiprocessing.Process(name='nonblock',target=\
        wait_for_event_timeout,args=(e,2))
    w2.start()
    print('main : waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main : event is set')
    
    