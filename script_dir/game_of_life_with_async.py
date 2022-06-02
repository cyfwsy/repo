'''用协程实现 game of life'''
import asyncio
import time
import random

ALIVE = '*'
EMPTY = '-'

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

async def temp_sleep(t):
    time.sleep(t)

async def count_neighbors(y,x,get):
    # ram_data = random.randint(20, 40)
    # time.sleep(0.5)
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

async def game_logic(state,neighbors):
    # ram_data = random.randint(10,30)
    # time.sleep(0.05) # 模拟在状态迁移时 i/o 花费的时间延迟，每个单元格可以认为分布在不同的物理地址
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY # Die
        elif neighbors > 3:
            return EMPTY # Die
    else:
        if neighbors == 3:
            return ALIVE #Regenerate
    return state

async def step_cell(y,x,get,set):
    state = get(y,x)
    neighbors = await count_neighbors(y,x,get)
    next_state = await game_logic(state,neighbors)
    await temp_sleep(0.005)
    set(y,x,next_state)

async def simulate(grid):
    next_grid = Grid(grid.height,grid.width)

    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(y,x,grid.get,next_grid.set) # fan_out
            tasks.append(task)
    await asyncio.gather(*tasks) # fan_in
    return next_grid

if __name__ == '__main__':
    grid = Grid(5, 9)
    grid.set(0, 3, ALIVE)
    grid.set(1, 4, ALIVE)
    grid.set(2, 2, ALIVE)
    grid.set(2, 3, ALIVE)
    grid.set(2, 4, ALIVE)
    for i in range(5):
        print(grid)
        grid = asyncio.run(simulate(grid))
