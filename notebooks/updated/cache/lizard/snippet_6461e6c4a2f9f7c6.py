def in_base(self, base):
    if base == self.base:
        return copy.deepcopy(self)
    result, _ = Radices.from_rational(self.as_rational(), base)
    return result