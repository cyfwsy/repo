from copy import deepcopy

def dfs_grid(grid,i,j,mark='X',free='.'):
    height = len(grid)
    width = len(grid[0])
    to_visit = [(i,j)]
    grid[i][j] = mark
    while to_visit:
        i1,j1 = to_visit.pop()
        for i2,j2 in [(i1+1,j1),(i1,j1+1),(i1-1,j1),(i1,j1-1)]:
            if 0 <= i2 < height and 0 <= j2 < width and grid[i2][j2] == free:
                grid[i2][j2] = mark
                print((i2,j2),end=',')
                to_visit.append((i2,j2))    
                
grid = [['.','.','#','#','#','#','#'],
        ['#','.','.','#','#','#','#'],
        ['#','.','.','#','#','#','#'],
        ['.','.','.','#','#','#','#'],
        ['#','#','.','#','#','#','#'],
        ['#','#','.','.','.','.','#'],
        ['.','.','.','#','#','#','#'],
        ]
grid_1 = deepcopy(grid)
dfs_grid(grid_1,3,2)
print('/n')
print('----------------------------------------------')
print(grid)
print('----------------------------------------------')
print(grid_1)
    