def _itemsLoadedDone(self, data):
    if data is None:
        return
    self.continuation = data.get('continuation', None)
    self.lastUpdated = data.get('updated', None)
    self.lastLoadLength = len(data.get('items', []))
    self.googleReader.itemsToObjects(self, data.get('items', []))
    self.lastLoadOk = True