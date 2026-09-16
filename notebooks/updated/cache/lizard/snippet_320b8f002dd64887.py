def getUpdates(self):
    ret = self._er.execQuery(self)
    if ret and 'recentActivityEvents' in ret:
        return ret['recentActivityEvents']
    return {}