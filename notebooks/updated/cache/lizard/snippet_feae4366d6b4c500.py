def updateMetadata(self, metadataFile):
    ip = ItemParameter()
    ip.metadata = metadataFile
    res = self.userItem.updateItem(itemParameters=ip, metadata=metadataFile)
    del ip
    return res