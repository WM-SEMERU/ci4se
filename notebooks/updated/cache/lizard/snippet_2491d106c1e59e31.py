def isSurrounded(self):
    malefics = [const.MARS, const.SATURN]
    return self.__sepApp(malefics, aspList=[0, 90, 180])