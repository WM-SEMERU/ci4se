def update(self, other):
    if type(self) != type(other):
        return NotImplemented
    else:
        if other.bad:
            self.error = other.error
            self.bad = True
        self._fieldDict.update(other._fieldDict)