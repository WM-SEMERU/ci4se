def free_symbols(self):
    return set.union(self.S.free_symbols, self.L.free_symbols, self.H.
        free_symbols)