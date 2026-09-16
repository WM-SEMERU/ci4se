def complement(self, *args):
    universe = self.union()
    to_diff = self.union(*args)
    return universe.difference(to_diff)