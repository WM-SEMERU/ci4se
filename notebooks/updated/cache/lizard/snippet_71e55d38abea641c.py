def getAlgorithmInstance(self, layer='L2', column=0):
    assert column >= 0 and column < self.numColumns, 'Column number not in valid range'
    if layer == 'L2':
        return self.L2Columns[column].getAlgorithmInstance()
    elif layer == 'L4':
        return self.L4Columns[column].getAlgorithmInstance()
    else:
        raise Exception("Invalid layer. Must be 'L4' or 'L2'")