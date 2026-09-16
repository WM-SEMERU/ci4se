def AddDir(self, dirpath):
    if dirpath not in self._dirs:
        self._dirs.add(dirpath)
        return True
    return False