def free_symbols(self):
    return set([sym for sym in self.term.free_symbols if sym not in self.
        bound_symbols])