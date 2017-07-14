import MoveRecorder
import NumericToAlphabeticConverter
import math


class Move:
    def __init__(self, type):
        self.displacement = self.typeToMovement(type);
        self.next = None;
        self.previous = None;
        self.isLastCalculated = False;
        self.type = type;
        self.sonarInfo = [];

    def typeToMovement(self, type):
        silence = [];

        for x in range(-4, 5):
            if x != 0:
                silence.append([x, 0])
                silence.append([0, x])

        return {
            'north': [[0, -1]],
            'south': [[0, 1]],
            'east': [[1, 0]],
            'west': [[-1, 0]],
            'silence': silence
        }[type]

    # returns a boolean. will casue odd behaviour if usage of start and possible positions are mixed.
    def validateMove(self, x, y, special=False):

        tempPosition = [];
        tempInPath = [];
        tempInPath.append(MoveRecorder.MoveRecorder.map[x][y]);

        if self.isLastCalculated:
            reaction = self.reversePath(x, y);
            for item in reaction:
                tempInPath.append(item);
                item.inPath = True;

        for move in self.displacement:

            coordinates = self.prepareNewCoordinate(move, x, y);
            flag = self.checkIfAllCoordinatesAreValid(coordinates);

            restraints = self.buildRestraints();
            flag2 = True;
            for item in restraints:
                flag2 = False;
                if coordinates[-1][0] == item[0] and coordinates[-1][1] == item[1]:
                    flag2 = True;
                    break

            if flag and flag2:
                newTileCoordinate = coordinates[-1];

                # at the end of chain. Does not add the last tile of the path.
                if self.next == None:
                    tempPosition.append(newTileCoordinate)
                    continue

                # not at the end of chain. adds current tile to path and continues in the chain.
                # placement of VV operation causes error in the check coordinates.
                MoveRecorder.MoveRecorder.map[x][y].inPath = True;
                reaction = self.next.validateMove(newTileCoordinate[0], newTileCoordinate[1]);
                if len(reaction) != 0:
                    for item in reaction:
                        tempPosition.append(item);

        for item in tempInPath:
            item.inPath = False;

        return tempPosition;

    def isOutOfBounds(self, newLocation):
        if newLocation[0] > 14 or newLocation[0] < 0: return True;
        if newLocation[1] > 14 or newLocation[1] < 0: return True;

        return False;

    # could go wrong if multiple paths are returned to the last calculated.
    # WARNING HIGHLY EXPERIMENTAL!!!
    # made cahnges to this do work with silence.
    def reversePath(self, x, y):
        tempPaths = [];
        if len(self.displacement) == 1:
            move = self.displacement[0];
            newTileCoordinate = [[x - move[0], y - move[1]]];
            flag = self.checkIfAllCoordinatesAreValid(newTileCoordinate);

            if flag:
                newTileCoordinate = newTileCoordinate[0];

                if self.previous != None:
                    reaction = self.previous.reversePath(newTileCoordinate[0], newTileCoordinate[1]);
                    if reaction != False:
                        if len(reaction) != 0:
                            for item in reaction:
                                tempPaths.append(item);

                tempPaths.append(MoveRecorder.MoveRecorder.map[newTileCoordinate[0]][newTileCoordinate[1]]);
                return tempPaths;

            else:
                return tempPaths;

        else:
            if self.isLastCalculated:
                return tempPaths;
            else:
                return False;

    def prepareNewCoordinate(self, move, x, y):
        tempCoords = [];

        if self.isLastCalculated:
            newTileCoordinate = [x, y];
            tempCoords.append(newTileCoordinate);
        else:
            if move[0] != 0:
                tempNumber = move[0];
            else:
                tempNumber = move[1];

            if tempNumber < 0:
                start = -1;
            else:
                start = 1;
            for number in range(1, (tempNumber * start) + 1):
                number = number * start;
                if move[0] != 0:
                    newTileCoordinate = [x + number, y];
                else:
                    newTileCoordinate = [x, y + number];

                tempCoords.append(newTileCoordinate);

        return tempCoords

    def checkIfAllCoordinatesAreValid(self, list):
        flag = True;
        for item in list:
            newTileCoordinate = item;

            if self.isOutOfBounds(newTileCoordinate):
                flag = False;
                break;

            # add loop over movement to check for islands during silence.
            if MoveRecorder.MoveRecorder.map[newTileCoordinate[0]][newTileCoordinate[1]].isClear() == False or \
                            MoveRecorder.MoveRecorder.map[newTileCoordinate[0]][
                                newTileCoordinate[1]].inPath == True:
                flag = False;
                break;

        return flag;

    def addInfo(self, list):
        list[1] = int(list[1]) - 1;
        self.sonarInfo.append(list);

    def removeInfo(self):
        if len(self.sonarInfo) != 0:
            del self.sonarInfo[-1];
            return True;
        return False;

    def buildRestraints(self):
        tempRestraints = [];
        for item in self.sonarInfo:
            if item[0] != 'z':
                rowNumber = NumericToAlphabeticConverter.NumericToAlphaBeticConverter.alphabetToNumeric(item[0]);
                for y in range(0, 15):
                    tempRestraints.append([rowNumber, y]);

            if int(item[1]) != 0:
                for x in range(0, 15):
                    tempRestraints.append([x, (int(item[1]))]);

            if int(item[2]) != 0:
                reaction = self.zoneToRestraints(item[2]);
                for item in reaction:
                    tempRestraints.append(item);

        tempRestraints = self.cleanRestraints(tempRestraints);
        return tempRestraints;

    def zoneToRestraints(self, zoneNumber):
        tempList = [];
        zoneX = (int(zoneNumber) - 1) % 3 * 5;
        zoneY = math.floor((int(zoneNumber) - 1) / 3) * 5;
        for x in range(0, 5):
            for y in range(0, 5):
                tempList.append([x + zoneX, y + zoneY])

        return tempList;

    def cleanRestraints(self, list):
        tempRestraints = [];

        for item in list:
            if item not in tempRestraints:
                tempRestraints.append(item);
            else:
                tempRestraints.remove(item);
        return tempRestraints;
