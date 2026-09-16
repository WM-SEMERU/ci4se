def populateFromRow(self, peerRecord):
    self.setUrl(peerRecord.url).setAttributesJson(peerRecord.attributes)
    return self