from typing import List
from PIL import Image

class Tile:
    def __init__(self,image:Image.Image,sides:List[str]):
        """the order of the side is [up,right,bottom,left]"""
        self.image = image
        self.sides = sides

    def rotate(self,n:int=1):
        """rotate the image of the tile + the sides n times"""
        newImage:Image.Image = self.image.rotate(90*n)
        newSides:List[str] = [self.sides[(x+n)%4] for x in range(len(self.sides))]
        return Tile(newImage,newSides)
    
    def match(self,other, sideN:int) -> bool:
        """check if the side of self matches with the corresponding side of the other"""
        return self.sides[sideN] == other.sides[(sideN+2) % 4][::-1]
    
    
    def __repr__(self) -> str:
        return str(self.sides)

    def __eq__(self, other) -> bool:
        return (self.sides==other.sides) and (list(self.image.getdata()) == list(other.image.getdata()))


if __name__ == '__main__':
    chemin = 'tiles/circuit/'
    tile0 = Tile(Image.open(chemin+'4.png'),['ABB','BCB','BBA','AAA'])
    tile1 = Tile(Image.open(chemin+'5.png'),['ABB','BBB','BBB','BBA'])
    print(tile0.match(tile1,2))
