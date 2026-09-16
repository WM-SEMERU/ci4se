def GetStat(self):
    if self._stat_object is None:
        self._stat_object = self._GetStat()
    return self._stat_object