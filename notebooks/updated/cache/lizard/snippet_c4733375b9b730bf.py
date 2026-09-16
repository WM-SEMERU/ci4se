def populateFromRow(self, continuousSetRecord):
    self._filePath = continuousSetRecord.dataurl
    self.setAttributesJson(continuousSetRecord.attributes)