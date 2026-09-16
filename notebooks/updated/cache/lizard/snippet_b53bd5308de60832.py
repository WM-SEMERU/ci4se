def getlevel(self, threshold):
    if len(self._input) <= 1:
        return self._input
    if not self.__cluster_created:
        self.cluster()
    return self._data[0].getlevel(threshold)