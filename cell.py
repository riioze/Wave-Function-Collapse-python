from tile import *
from random import choice
from utils import load_batch
from PIL import Image


class Cell:
    def __init__(self,tileList:List[Tile]):
        self.collapsed:bool = False
        self.options : List[Tile] = [t for t in tileList]
    
    def collapse(self):
        self.collapsed = True
        self.options = [choice(self.options)]
    
    def update(self,neighbor:Tile,neighborSide:int):
        newoptions : List[Tile] = [option for option in self.options if option.match(neighbor,neighborSide)]
        self.options = newoptions

    def __repr__(self) -> str:
        if self.collapsed:
            return 'Collapsed'
        else:
            return f'Uncollapsed({len(self.options)})'
    
    
    def __getitem__(self,index:int) -> Tile:
        return self.options[index]

Grid = List[List[Cell]]      


def collapsedGrid(grid:Grid) -> List[List[int]]:
    r : List[List[int]] = []
    l:List[int]
    for ligne in grid:
        l=[]
        for c in ligne:
            if c.collapsed:
                l.append(0)
            else:
                l.append(len(c.options))
        r.append(l)

    return r

def show_grid(grid:Grid) -> Image.Image:
    nx = len(grid[0])
    ny = len(grid)
    cw = grid[0][0][0].image.width
    ch = grid[0][0][0].image.height
    w = nx*cw
    h = ny*ch
    r = Image.new(grid[0][0][0].image.mode,(w,h),color=(0,0,0))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[x][y].collapsed:
                r.paste(grid[x][y][0].image,(x*cw,y*ch))


    return r


if __name__ == '__main__':
    allTiles = load_batch('tiles/circuit',3)
    
    print(allTiles)
    print(len(allTiles))