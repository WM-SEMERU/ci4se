def _hole_start(self, position, ignore=None):
    for lindex in reversed(range(0, position)):
        for starting in self.starting(lindex):
            if not ignore or not ignore(starting):
                return lindex
    return 0