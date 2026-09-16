def getDict(self):
    badList = self.checkSetSaveEntries(doSave=False)
    if badList:
        self.processBadEntries(badList, self.taskName, canCancel=False)
    return self._taskParsObj.dict()