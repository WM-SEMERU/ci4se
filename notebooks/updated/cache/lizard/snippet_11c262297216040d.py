def commit(self):
    while len(self.__buffer) > 0:
        self.__run(self.__buffer.pop(0))