def readTable(self, tableName):
    lock_and_call(lambda : self._impl.readTable(tableName), self._lock)