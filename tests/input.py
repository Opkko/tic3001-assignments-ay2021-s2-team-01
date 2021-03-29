from circular_shift import CircularShift

class Input:
    def __init__(self, inputFile, ignoredFile, requiredFile):
        self.__inputList = self.__getlines(inputFile)
        self.__ignoredList = self.__getlines(ignoredFile)
        self.__requiredList = self.__getlines(requiredFile)
        self.__callcircularshift()

    def __getlines(self, filename):
        with open(filename) as file:
            lines = [line.strip() for line in file]
            return lines

    def __callcircularshift(self):
        CircularShift(self.__inputList, self.__ignoredList, self.__requiredList)
