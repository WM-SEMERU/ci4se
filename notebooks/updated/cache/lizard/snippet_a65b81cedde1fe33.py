def close(self):
    if not hasattr(self, 'tiffs'):
        return
    for tif in self._tiffs.values():
        if tif._fd:
            tif._fd.close()
            tif._fd = None