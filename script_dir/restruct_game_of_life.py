'''使用队列来完成线程任务'''
from queue import Queue
import random
import time
from threading import Thread

class ClosableQueue(Queue):
    SENTINEL = object()
    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # Cause the thread to exit
                yield item
            finally:
                self.task_done()

class StoppableWorker(Thread):
    def __init__(self,func,in_queue,out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue: # 迭代队列，取出加工品
            result = self.func(item) #对加工品进行加工
            self.out_queue.put(result) #将半成品放入下一阶段队列

def step_cell(y,x,get,set):
    state = get(y,x)
    neighbors = count_neighbors(y,x,get)
    next_state = game_logic(state,neighbors)
    set(y,x,next_state)

# game_logic 有 i/o 延时
def game_logic(state,neighbors):
    ram_data = random.randint(10,30)
    time.sleep(1/ram_data) # 模拟在状态迁移时 i/o 花费的时间延迟，每个单元格可以认为分布在不同的物理地址
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY # Die
        elif neighbors > 3:
            return EMPTY # Die
    else:
        if neighbors == 3:
            return ALIVE #Regenerate
    return state

def game_logic_thread(item):
    y,x,state,neighbors = item
    try:
        next_state = game_logic(state,neighbors)
    except Exception as e:
        next_state = e
    return (y,x,next_state)

ALIVE = '*'
EMPTY = '-'

class SimulationError(Exception):
    pass

class Grid:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self,y,x):
        return self.rows[y % self.height][x % self.width]
    def set(self,y,x,state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        temp = []
        for y in range(self.height):
            str1 = ''.join(self.rows[y])
            temp.append(str1 + '\n')
        return ''.join(temp)

def count_neighbors(y,x,get):
    n_ = get(y-1,x+0) # North
    ne = get(y-1,x+1) # Northeast
    e_ = get(y+0,x+1) # East
    se = get(y+1,x+1) # Southeast
    s_ = get(y+1,x+0) # South
    sw = get(y+1,x-1) # Southwest
    w_ = get(y+0,x-1) # West
    nw = get(y-1,x-1) # Northwest
    neighbor_states = [n_,ne,e_,se,s_,sw,w_,nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

def simulate_pipeline(grid,in_queue,out_queue):
    for y in range(grid.height):
        for x in range(grid.width):
            state = grid.get(y,x)
            neighbors = count_neighbors(y,x,grid.get)
            in_queue.put((y,x,state,neighbors)) # Fan out
    in_queue.join()
    out_queue.close()
    next_grid = Grid(grid.height,grid.width)
    for item in out_queue:
        y,x,next_state = item
        if isinstance(next_state,Exception):
            raise SimulationError(y,x) from next_state
        next_grid.set(y,x,next_state)
    return next_grid

if __name__ == '__main__':
    ALIVE = '*'
    EMPTY = '-'

    in_queue = ClosableQueue()
    out_queue = ClosableQueue()
    grid = Grid(6,10)
    grid.set(0, 3, ALIVE)
    grid.set(1, 4, ALIVE)
    grid.set(2, 2, ALIVE)
    grid.set(2, 3, ALIVE)
    grid.set(2, 4, ALIVE)
    grid.set(3, 5, ALIVE)
    grid.set(3, 8, ALIVE)

    # Start the threads upfront
    threads = []
    for _ in range(6):
        thread = StoppableWorker(game_logic_thread, in_queue, out_queue)
        thread.start()
        threads.append(thread)

    print(grid)
    for i in range(8):
        grid = simulate_pipeline(grid,in_queue,out_queue)
        print(grid)

    for thread in threads:
        in_queue.close()
    for thread in threads:
        thread.join()




