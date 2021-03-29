from output import Output

class AlphabetSort:
    def __init__(self, shifted):
        self.__shifted = shifted
        self.__getsorted()
        self.__calloutput()

    def __getsorted(self):
        return self.__shifted.sort(key=str.casefold)

    def __calloutput(self):
        Output(self.__shifted)
        