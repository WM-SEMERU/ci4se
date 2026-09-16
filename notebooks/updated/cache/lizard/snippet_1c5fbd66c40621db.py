def committed(self):
    if self.__deleting:
        self.deleted()
        if not self.__legacy__:
            self.store.objectCache.uncache(self.storeID, self)
            self.__store = None
    self.__justCreated = False