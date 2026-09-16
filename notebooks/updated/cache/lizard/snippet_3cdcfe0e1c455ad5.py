def FullJournalName(self):
    global abbrevDict
    if abbrevDict is None:
        abbrevDict = getj9dict()
    if self.isJournal():
        return abbrevDict[self.journal][0]
    else:
        return None