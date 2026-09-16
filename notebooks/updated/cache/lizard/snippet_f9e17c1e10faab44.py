def currentVersion(self):
    if self._currentVersion is None:
        self.__init(self._url)
    return self._currentVersion