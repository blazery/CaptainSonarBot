class Tile:
    def __init__(self, x, y):
        self.xPos = x;
        self.yPos = y;
        self.isWater = True;
        self.inPath = False;

    def isClear(self):
        return self.isWater;
