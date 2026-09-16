def getWordAtOffset(self, offset):
    return datatypes.WORD.parse(utils.ReadData(self.getDataAtOffset(offset, 2))
        )