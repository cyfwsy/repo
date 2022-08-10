"thread_barrier_example,多线程等待在barrier上，同时到达时，全部结束等待"
import threading
def worker(b):
    b.wait()
    print(f'in one of threads',threading.get_native_id())
    
def main(parties):
    b = threading.Barrier(parties+1)
    for i in range(parties):
        t = threading.Thread(target=worker,args=(b,))
        t.start()
    b.wait()
    print(f'in main thread',threading.get_native_id())
    
if __name__ == '__main__':
    main(3)
        
    