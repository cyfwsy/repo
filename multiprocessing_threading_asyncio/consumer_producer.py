import multiprocessing
import time
class Consumer(multiprocessing.Process):
    def __init__(self,task_queue,result_queue):
        super().__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue
        
    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                #Poison pill means shutdown
                print('{} : exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}:{}'.format(proc_name,next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)
            
class Task:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        
    def __call__(self):
        time.sleep(0.3) # pretend to take time to do the work
        return '{self.a} * {self.b} = {product}'.format(self=self,\
            product=self.a * self.b)
        
    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)
    
if __name__ == '__main__':
    # Establish communication queue
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    
    # Start Consumers
    num_consumers = multiprocessing.cpu_count() 
    print('Creating {} Consumers'.format(num_consumers))
    consumers = [Consumer(tasks,results)
                 for i in range(num_consumers)]
    for w in consumers:
        w.start()
    
    # Enqueue jobs
    num_jobs = 50
    for i in range(num_jobs):
        tasks.put(Task(i,i))
        
    # Add a Poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)
        
    # waiting for all of the  tasks to finish
    tasks.join()
    
    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:',result)
        num_jobs -= 1
    
            
                