'''使用线程池完成 fan_out fan_in'''
from restruct_game_of_life import ALIVE, EMPTY, count_neighbors, game_logic, step_cell, Grid
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class LockingGrid(Grid):
    def __init__(self,height,width):
        super().__init__(height,width)
        self.lock = Lock()

    def __str__(self):
        with self.lock:
            return super().__str__()
    def get(self,y,x):
        with self.lock:
            return super().get(y,x)
    def set(self,y,x,state):
        with self.lock:
            super().set(y,x,state)

def simulate_pool(pool,grid):
    next_grid = LockingGrid(grid.height,grid.width)
    futures = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (y,x,grid.get,next_grid.set)
            future = pool.submit(step_cell,*args) # Fan_out
            futures.append(future)
    for future in futures:
        future.result()
    return next_grid

if __name__ == '__main__':
    grid = LockingGrid(5,9)
    grid.set(0,3,ALIVE)
    grid.set(1,4,ALIVE)
    grid.set(2,2,ALIVE)
    grid.set(2,3,ALIVE)
    grid.set(2,4,ALIVE)

    with ThreadPoolExecutor(max_workers=10) as pool:
        for i in range(5):
            print(grid)
            grid = simulate_pool(pool,grid)