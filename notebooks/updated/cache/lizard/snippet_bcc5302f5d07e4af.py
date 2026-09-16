def loadItems(self, excludeRead=False, loadLimit=20, since=None, until=None):
    self.clearItems()
    self.loadtLoadOk = False
    self.lastLoadLength = 0
    self._itemsLoadedDone(self._getContent(excludeRead, None, loadLimit,
        since, until))