def populateFromRow(self, featureSetRecord):
    self._dbFilePath = featureSetRecord.dataurl
    self.setAttributesJson(featureSetRecord.attributes)
    self._db = Gff3DbBackend(self._dbFilePath)