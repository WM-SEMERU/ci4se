def previous(self):
    if self.index - 1 >= 0:
        self.index = self.index - 1
    elif self.stack:
        self.gametree = self.stack.pop()
        self.index = len(self.gametree) - 1
    else:
        raise GameTreeEndError
    self.node = self.gametree[self.index]
    self.nodenum = self.nodenum - 1
    self._setChildren()
    self._setFlags()
    return self.node