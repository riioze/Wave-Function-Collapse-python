from tile import *
from random import choice
from utils import load_batch
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

if __name__ == '__main__':
    allTiles = load_batch('tiles/circuit',3)
    
    print(allTiles)
    print(len(allTiles))