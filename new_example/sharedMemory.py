from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager
from re import S
def do_worker1(shm_list):
    for index,item in enumerate(shm_list):
        shm_list[index] = item * item
        
def do_worker2(shm_list):
    for index,item in enumerate(shm_list):
        shm_list[index] = item + 1
        
if __name__ ==   '__main__'  :  
    with SharedMemoryManager()  as smm:
        sha_l = smm.ShareableList(range(10))
        p1 = Process(target=do_worker1,args=(sha_l,))
        p2 = Process(target=do_worker2,args=(sha_l,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(sha_l)
        
        
        