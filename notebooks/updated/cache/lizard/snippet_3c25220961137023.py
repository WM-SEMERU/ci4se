def last(self):
    self.__file.seek(0, 2)
    data = self.get(self.length - 1)
    return data