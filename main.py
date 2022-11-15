from cell import *
from typing import Tuple


dim:Tuple[int,int] = (2,2)
grid : List[List[Cell]] = []


if __name__ == '__main__':
    allTiles = load_batch('tiles/circuit',3)
    