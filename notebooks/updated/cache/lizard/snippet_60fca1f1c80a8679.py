def canMove(self):
    if not self.filled():
        return True
    for y in self.__size_range:
        for x in self.__size_range:
            c = self.getCell(x, y)
            if x < self.__size - 1 and c == self.getCell(x + 1, y
                ) or y < self.__size - 1 and c == self.getCell(x, y + 1):
                return True
    return False