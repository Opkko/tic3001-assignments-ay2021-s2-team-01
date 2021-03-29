from collections import deque
from alphabetical_sort import AlphabetSort

class CircularShift:
    def __init__(self,inputList, ignoredList, requiredList):
        self.__isIgnored = False
        self.__isRequired = False
        self.__inputList = inputList
        self.__ignoredList = ignoredList
        self.__requiredList = requiredList
        self.__shifted = []
        self.__getshifted()
        self.__callalphabetsort()

    def __getshifted(self):
        for line in self.__inputList:
            wordlist = line.split(" ")
            self.deq = deque(wordlist)

            for i in range(0, len(self.deq)):
                self.deq.rotate()
                self.__iswordinlist()
                self.__cases()

    def __iswordinlist(self):
        for word in self.__ignoredList:
            self.__isIgnored = False
            if self.deq[0].casefold() == word.casefold():
                self.__isIgnored = True
                break
        
        for word in self.__requiredList:
            self.__isRequired = False
            if self.deq[0].casefold() == word.casefold():
                self.__isRequired = True
                break

    def __cases(self):
        if len(self.__requiredList) > 0 and self.__isRequired:
            self.__appendshiftedlist()

        elif len(self.__ignoredList) > 0 and len(self.__requiredList) == 0:
            if not self.__isIgnored:
                self.__appendshiftedlist()

        elif len(self.__requiredList) == 0 and len(self.__requiredList) == 0:
            self.__appendshiftedlist()
    
    def __appendshiftedlist(self):   
        jointostring = ' '.join(self.deq) 
        self.__shifted.append(jointostring)
                
    def __callalphabetsort(self):
        AlphabetSort(self.__shifted)
