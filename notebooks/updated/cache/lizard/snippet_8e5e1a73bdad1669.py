def getCheckpointFile(self):
    checkpointFile = self._jrdd.rdd().getCheckpointFile()
    if checkpointFile.isDefined():
        return checkpointFile.get()