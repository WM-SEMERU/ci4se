def findInvariantPartitioning(self):
    symorders = self.symorders[:]
    _range = range(len(symorders))
    while 1:
        pos = self.findLowest(symorders)
        if pos == -1:
            self.symorders = symorders
            return
        for i in _range:
            symorders[i] = symorders[i] * 2 + 1
        symorders[pos] = symorders[pos] - 1
        symorders = self.findInvariant(symorders)