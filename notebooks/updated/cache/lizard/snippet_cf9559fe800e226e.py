def loadSignal(self, name, start=None, end=None):
    entry = self._getCacheEntry(name)
    if entry is not None:
        from analyser.common.signal import loadSignalFromWav
        return loadSignalFromWav(entry['path'], start=start, end=end)
    else:
        return None