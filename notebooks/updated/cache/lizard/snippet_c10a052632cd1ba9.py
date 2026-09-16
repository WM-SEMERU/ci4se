def wherefunc(self, func, fieldname=None, negate=False):
    if fieldname is not None:
        if negate:
            return self.mask([(not func(value)) for value in self[fieldname]])
        else:
            return self.mask([func(value) for value in self[fieldname]])
    elif negate:
        return self.mask([(not func(row)) for row in self])
    else:
        return self.mask([func(row) for row in self])