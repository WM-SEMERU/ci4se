def populateFromRow(self, row):
    self._dbFilePath = row[b'dataUrl']
    self._db = SqliteRnaBackend(self._dbFilePath)
    self.getRnaQuantMetadata()