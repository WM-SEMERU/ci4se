def AddFile(self, filepath):
    if filepath not in self._files:
        self._files.add(filepath)
        return True
    return False