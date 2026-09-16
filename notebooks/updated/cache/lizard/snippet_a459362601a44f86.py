def getPluginsList(self, enable=True):
    if enable:
        return [p for p in self._plugins if self._plugins[p].is_enable()]
    else:
        return [p for p in self._plugins]