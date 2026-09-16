def getFilesystemStats(self, fs):
    if self._mapFSpathDev is None:
        self._initFilesystemInfo()
    return self._diskStats.get(self._mapFSpathDev.get(fs))