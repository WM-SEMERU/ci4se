def overlap(self, other):
    if not self or not other:
        return False
    if self < other:
        a, b = self, other
    else:
        a, b = other, self
    if a.upper_inf or b.lower_inf:
        return True
    return (a.upper > b.lower or a.upper == b.lower and a.upper_inc and b.
        lower_inc)