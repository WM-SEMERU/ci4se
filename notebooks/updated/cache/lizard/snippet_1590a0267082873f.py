def __moveLineOrCol(self, line, d):
    nl = [c for c in line if c != 0]
    if d == Board.UP or d == Board.LEFT:
        return nl + [0] * (self.__size - len(nl))
    return [0] * (self.__size - len(nl)) + nl