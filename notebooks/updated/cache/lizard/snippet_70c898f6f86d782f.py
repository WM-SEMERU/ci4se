def getDriverName(self, nDriver, pchValue, unBufferSize):
    fn = self.function_table.getDriverName
    result = fn(nDriver, pchValue, unBufferSize)
    return result