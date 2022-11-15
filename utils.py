from tile import Tile
from typing import List,Tuple,Dict
import glob
from PIL import Image
from random import choice

ABC:str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def load_batch(path:str,div:int) -> List[Tile]:
    """load a batch of tile in a directory"""
    r:List[Tile] = []
    lImage = [Image.open(p) for p in glob.glob(path+'/*.png')]
    colors = get_colors(lImage)
    w,h = lImage[0].size
    if div == 1:
        pass

    else:
        for image in lImage:
            sides:List[str] = []
            #Top
            top:str=''
            for x in range(div):
                top+=colors[image.getpixel((x*int(w/(div-1))-x,0))]
            sides.append(top)
        
            #Right
            right:str = ''
            for x in range(div):
                right+=colors[image.getpixel((w-1,x*int(h/(div-1))-x))]
            sides.append(right)

            #Bottom
            bottom:str=''
            for x in range(div)[::-1]:
                bottom+=colors[image.getpixel((x*int(w/(div-1))-x,h-1))]

            sides.append(bottom)

            #Left
            left:str = ''
            for x in range(div)[::-1]:
                left+=colors[image.getpixel((0,x*int(h/(div-1))-x))]
            sides.append(left)

            t = Tile(image,sides)
            tbatch=[t]

            
            for a in range(1,4):
                if not t.rotate(a) in tbatch:
                    tbatch.append(t.rotate(a))
            
            r+=tbatch


    return r


def get_colors(imgs:List[Image.Image]) -> Dict[Tuple[int,int,int],str]:
    r : Dict[Tuple[int,int,int],str] = {}

    lindex = 0

    for img in imgs:
        colors = img.getcolors()
        for cnum,color in colors:
            if not color in r.keys():
                r[color] = ABC[lindex]  # type: ignore
                lindex+=1



    return r


def choose(grid:List[List[int]]) -> Tuple[int,int]:
    min_val = float('+inf')

    for line in grid:
        for n in line:
            if n < min_val and n > 0:
                min_val = n
    all_options : List[Tuple[int,int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == min_val:
                all_options.append((x,y))
    return choice(all_options)

if __name__ == '__main__':
    b = load_batch('tiles/circuit',3)