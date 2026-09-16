def calculate2d(self, force=True):
    for ml in (self.__reagents, self.__reactants, self.__products):
        for m in ml:
            m.calculate2d(force)
    self.fix_positions()