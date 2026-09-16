def getUnitCost(self, CorpNum):
    result = self._httpget('/CloseDown/UnitCost', CorpNum)
    return float(result.unitCost)