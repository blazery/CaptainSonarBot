import Tile


class MapCreator:
    @staticmethod
    def createMapA():

        tempMap = [];

        for x in range(0, 15):
            tempMap.append([]);
            for y in range(0, 15):
                tempMap[x].append(Tile.Tile(x, y));


        tempMap[2][1].isWater = False;
        tempMap[2][2].isWater = False;

        tempMap[6][1].isWater = False;

        tempMap[8][2].isWater = False;
        tempMap[8][3].isWater = False;

        tempMap[12][1].isWater = False;
        tempMap[12][2].isWater = False;
        tempMap[13][1].isWater = False;

        tempMap[1][6].isWater = False;
        tempMap[1][7].isWater = False;

        tempMap[3][6].isWater = False;
        tempMap[3][7].isWater = False;
        tempMap[3][8].isWater = False;

        tempMap[6][6].isWater = False;
        tempMap[6][7].isWater = False;
        tempMap[7][8].isWater = False;

        tempMap[8][6].isWater = False;

        tempMap[11][8].isWater = False;
        tempMap[12][8].isWater = False;
        tempMap[13][8].isWater = False;
        tempMap[0][12].isWater = False;

        tempMap[2][11].isWater = False;
        tempMap[3][10].isWater = False;

        tempMap[2][13].isWater = False;
        tempMap[3][14].isWater = False;

        tempMap[6][13].isWater = False;

        tempMap[7][11].isWater = False;

        tempMap[8][13].isWater = False;

        tempMap[11][11].isWater = False;
        tempMap[12][12].isWater = False;
        tempMap[13][13].isWater = False;

        return tempMap;
