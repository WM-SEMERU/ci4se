def contains_set(self, other):
    if other is self:
        return True
    return isinstance(other, RealNumbers) or isinstance(other, Integers)