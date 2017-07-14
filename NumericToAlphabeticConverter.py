class NumericToAlphaBeticConverter:
    @staticmethod
    def numberToAlphabet(number):
        return {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K',
            11: 'L',
            12: 'M',
            13: 'N',
            14: 'O'
        }.get(number);

    @staticmethod
    def alphabetToNumeric(letter):
        return {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'z': 99

        }.get(str(letter).lower());

    @staticmethod
    def numberInList(number):
        if int(number) >= 0 and int(number) <= 15:
            return True;
        else:
            return False;

    @staticmethod
    def letterInList(letter):
        result = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'z': 99

        }.get(str(letter).lower());

        if result != None:
            return True;
        else:
            return False;
