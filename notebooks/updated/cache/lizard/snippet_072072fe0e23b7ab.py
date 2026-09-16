def get_broks(self):
    res = copy.copy(self.broks)
    del self.broks[:]
    return res