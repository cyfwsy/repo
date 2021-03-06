'''使用队列，多线程任务完成生命游戏的进化'''
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

def game_logic(state,neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY # Die
        elif neighbors > 3:
            return EMPTY # Die
    else:
        if neighbors == 3:
            return ALIVE #Regenerate
    return state

def step_cell(y,x,get,set):
    state = get(y,x)
    neighbors = count_neighbors(y,x,get)
    next_state = game_logic(state,neighbors)
    set(y,x,next_state)

#开始 simulation
def simulate(grid):
    next_grid = Grid(grid.height,grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y,x,grid.get,next_grid.set)
    return next_grid

#测试Grid 类
grid = Grid(5,9)
grid.set(0,3,ALIVE)
grid.set(1,4,ALIVE)
grid.set(2,2,ALIVE)
grid.set(2,3,ALIVE)
grid.set(2,4,ALIVE)
print(grid)

for i in range(5):
    grid = simulate(grid)
    print(grid)