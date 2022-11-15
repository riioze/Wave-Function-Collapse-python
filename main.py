from cell import *
from typing import Tuple
from utils import choose
import os

allTiles = load_batch('tiles/circuit',3)
dim:Tuple[int,int] = 20,20

x,y = dim
grid : List[List[Cell]] = [[Cell(allTiles) for i in range(x)] for j in range(y)]



while collapsedGrid(grid) != [[0 for c in ligne] for ligne in grid]:
    collapsed = collapsedGrid(grid)
    choosed = choose(collapsed)
    x,y = choosed
    grid[y][x].collapse()
    for dir,dx,dy in [(2,-1,0),(3,0,1),(0,1,0),(1,0,-1)]:

        if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid) and not grid[y+dy][x+dx].collapsed:
            grid[y+dy][x+dx].update(grid[y][x][0],dir)
    

"""
    for opt in grid[0][0]:
        print(opt)
        opt.image.show()"""

    

img = show_grid(grid)
img.show()

yn = input('save(y/n)')
if yn == 'y':
    name = input('name')
    img.save('results/'+name+'.png')

