"深度優先找連通分量"
def dfs_grid(grid, i, j, mark, free):
    grid[i][j] = mark
    height = len(grid)
    width = len(grid[0])
    for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        if 0 <= ni < height and 0 <= nj < width:
            if grid[ni][nj] == free:
                dfs_grid(grid,ni,nj,mark,free)
                
def nb_connected_components_grid(grid,free="#"):
    nb_components = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j] == free:
                nb_components += 1
                dfs_grid(grid,i,j,str(nb_components),free)
    return nb_components

grid_1 = [['f','f','#','f','f','f','f','f','f','f'],
          ['f','f','#','#','#','f','f','f','f','f'],
          ['f','f','#','#','#','f','f','f','f','f'],
          ['f','f','#','#','f','f','f','f','f','f'],
          ['f','f','#','f','f','#','#','f','f','f'],
          ['f','f','f','f','#','#','f','f','f','f'],
          ['f','f','#','f','f','#','f','f','f','f'],
          ['f','f','#','#','f','#','#','#','f','f'],
          ['f','f','#','f','f','f','f','f','#','#']]
          
print(nb_connected_components_grid(grid_1))