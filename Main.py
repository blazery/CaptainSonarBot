import MoveRecorder
import NumericToAlphabeticConverter

recorder = MoveRecorder.MoveRecorder();

moves = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west',
    'si': 'silence',
    'l': 'silence',
};
lastMove = [];


def displayPosibilitiesInList(list):
    tempString = '';
    tempListOfMessages = [];
    tempNumber = 0;
    for item in list:
        if tempNumber == 5:
            tempNumber = 0;
            tempListOfMessages.append(tempString);
            tempString = '';

        tempString += '[' + NumericToAlphabeticConverter.NumericToAlphaBeticConverter.numberToAlphabet(
            item[0]) + ' , ' + str(item[1] + 1) + '] , ';
        tempNumber += 1;

    if tempString != '':
        tempListOfMessages.append(tempString);

    for item in tempListOfMessages:
        print(item);


def displayPosibilitiesOnMap(positions):
    base = recorder.possibleStart;
    line = '';
    counter = 0;
    linelist = [];

    for x in range(0, 15):
        for y in range(0, 15):
            if base[y][x] == True:
                line += chr(9781);
            else:
                line += chr(9775);
        linelist.append(line);
        line = '';

    if line != '':
        linelist.append(line);

    for item in positions:
        tempLine = list(linelist[item[1]]);
        tempLine[item[0]] = chr(9728);
        tempLine = ''.join(tempLine);
        linelist[item[1]] = tempLine;

    for item in linelist:
        print(item);
    return;


while True:
    inp = input('Movement direction: ');

    move = moves.get(inp);
    if move != None:
        reaction = recorder.addMove(move);
        print(' Possible Positions: ' + str(len(reaction)));
        if len(reaction) == 1:
            displayPosibilitiesInList(reaction);
        lastMove.append('m');

    else:
        if inp == 'c' or inp == 'calc':
            posibilities = recorder.calculatePosibilities();
            print(' Posibility length: ' + str(len(posibilities)));
            displayPosibilitiesInList(posibilities);
        elif inp == 'info' or inp == 'i' or inp == 'sonar':
            inp = input('input info, A,12,6 : ');
            if inp != 'c':
                listChar = inp.split(',');
                print(' ' + str(recorder.addInfoToLastMove(listChar)));
                lastMove.append('i');
        elif inp == 'u' or inp == 'undo':
            if len(lastMove) != 0:
                if lastMove[-1] == 'm':
                    print(recorder.removeLastMove());
                    del lastMove[-1];
                elif lastMove[-1] == 'i':
                    print(recorder.removeLastInfo());
                    del lastMove[-1];
                elif lastMove[-1] == 'r':
                    print('Ranges can not be undone reset all.');
    


        elif inp == 'q' or inp == 'quit':
            break
        elif inp == 'reset':
            recorder.clearMoves();
            print(' Everything restarted, clean slate achieved.')
        elif inp == 'm' or inp == 'map':
            posibilities = recorder.calculatePosibilities();
            print(' Possible Positions: ' + str(len(posibilities)));
            displayPosibilitiesOnMap(posibilities);
        elif inp == 'range':
            inp = input('Enter a range of movements: ');
            listChar = list(inp);

            number = 0;
            for item in listChar:
                direction = moves.get(item);
                if direction != None:
                    recorder.addMove(direction);

        lastMove.append('r');
