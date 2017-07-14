import Move
import MapCreator
import NumericToAlphabeticConverter


class MoveRecorder:
    map = MapCreator.MapCreator.createMapA();

    def __init__(self):
        self.firstMove = None;
        self.lastCalculatedMove = None;
        self.moveList = [];
        self.possiblePositions = [];
        self.possiblePositionsbuffer = [];
        self.possibleStart = self.createStartPointsFromMap();

    def selectMap(self, mapLetter):
        self.clearMoves();
        print('Game Restarted');

        if True:
            MoveRecorder.map = MapCreator.MapCreator.createMapA();
            return 'Map A selected.';
        elif mapLetter.lower() == 'b':
            return 'Map B selected.';

        MoveRecorder.map = MapCreator.MapCreator.createMapA();
        return 'Map A selected.';

    def addMove(self, type):
        self.moveList.append(Move.Move(type))

        if self.firstMove == None:
            self.firstMove = self.moveList[0];
        else:
            self.moveList[-2].next = self.moveList[-1];
            self.moveList[-1].previous = self.moveList[-2];

        return self.calculatePosibilities();

    def addInfoToLastMove(self, list):
        if len(list) != 3 or len(self.moveList) == 0: return

        var1 = NumericToAlphabeticConverter.NumericToAlphaBeticConverter.letterInList(list[0]);
        var2 = NumericToAlphabeticConverter.NumericToAlphaBeticConverter.numberInList(list[1]);
        var3 = int(list[2]) >= 0 and int(list[2]) < 10;
        if var1 and var2 and var3:
            self.moveList[-1].addInfo(list);
            return self.moveList[-1].sonarInfo;

    def clearMoves(self):
        self.firstMove = None;
        self.lastCalculatedMove = None;
        self.moveList = [];
        self.possiblePositions = [];
        self.possiblePositionsbuffer = [];
        self.possibleStart = self.createStartPointsFromMap();

    def removeLastMove(self):
        if len(self.moveList) == 0: return ' no moves to remove';

        if self.moveList[-1].isLastCalculated: self.lastCalculatedMove = None;

        del self.moveList[-1];
        if len(self.moveList) != 0:
            self.moveList[-1].next = None;
        else:
            self.firstMove = None;

        self.possiblePositions = self.possiblePositionsbuffer;
        return ' Move removed successfully';
        # might cause errors with the possible positions.

    def removeLastInfo(self):
        if len(self.moveList) == 0: return;
        if len(self.moveList[-1].sonarInfo) == 0: return;

        if self.moveList[-1].removeInfo():
            self.possiblePositions = self.possiblePositionsbuffer;
            return ' info deleted';
        else:
            return ' no info to delete';

    def createStartPointsFromMap(self):
        tempOptions = [];
        number = 0;
        for x in MoveRecorder.map:
            tempOptions.append([]);
            for y in x:
                if y.isClear():
                    tempOptions[number].append(True);
                else:
                    tempOptions[number].append(False);
            number += 1;
        return tempOptions;

    def cleanPossibilities(self, list):
        tempPossibilities = [];

        for item in list:
            if item not in tempPossibilities:
                tempPossibilities.append(item);

        return tempPossibilities;

    def calculatePosibilities(self):
        # checks in there is a last calculated point available.
        if len(self.moveList) == 0 or self.firstMove == None: return [];

        flag = False;
        for item in self.moveList:
            if item.isLastCalculated:
                flag = True;
                break
        # uses possible positions from the last confirmed move instead of all startPositions.
        if len(self.possiblePositions) != 0 and flag:
            tempPosibilities = self.checkFromPossiblePositions();
        else:
            tempPosibilities = self.checkFromStartPositions();

        for item in self.moveList:
            item.isLastCalculated = False;

        self.moveList[-1].isLastCalculated = True;
        self.lastCalculatedMove = self.moveList[-1];

        self.possiblePositionsbuffer = self.possiblePositions;
        self.possiblePositions = self.cleanPossibilities(tempPosibilities);
        return self.possiblePositions;

    def checkFromStartPositions(self):
        currentStartPointX = -1;

        tempPosibilities = [];

        for item in self.possibleStart:
            currentStartPointX += 1;
            currentStartPointY = -1;
            for field in item:
                currentStartPointY += 1;
                if field:
                    currentPointX = currentStartPointX;
                    currentPointY = currentStartPointY;
                    reaction = self.firstMove.validateMove(currentPointX, currentPointY);

                    if len(reaction) != 0:
                        for item in reaction:
                            tempPosibilities.append(item);

        return tempPosibilities;

    def checkFromPossiblePositions(self):
        tempPosibilities = [];

        for item in self.possiblePositions:
            reaction = self.lastCalculatedMove.validateMove(item[0], item[1]);
            if len(reaction) != 0:
                for item in reaction:
                    tempPosibilities.append(item);

        return tempPosibilities;
