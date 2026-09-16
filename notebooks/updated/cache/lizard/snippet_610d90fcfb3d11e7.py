def removeSingleCachedFile(self, fileStoreID):
    with self._CacheState.open(self) as cacheInfo:
        cachedFile = self.encodedFileID(fileStoreID)
        cachedFileStats = os.stat(cachedFile)
        assert cachedFileStats.st_nlink <= self.nlinkThreshold, 'Attempting to delete a global file that is in use by another job.'
        assert cachedFileStats.st_nlink >= self.nlinkThreshold, 'A global file has too FEW links at deletion time. Our link threshold is incorrect!'
        os.remove(cachedFile)
        if self.nlinkThreshold != 2:
            cacheInfo.cached -= cachedFileStats.st_size
        if not cacheInfo.isBalanced():
            self.logToMaster(
                'CACHE: The cache was not balanced on removing single file',
                logging.WARN)
        self.logToMaster("CACHE: Successfully removed file with ID '%s'." %
            fileStoreID)
    return None