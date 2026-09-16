def set_phases(self, literals=[]):
    if self.minicard:
        pysolvers.minicard_setphases(self.minicard, literals)