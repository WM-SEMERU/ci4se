def getCol(self, x):
    return [self.getCell(x, i) for i in self.__size_range]