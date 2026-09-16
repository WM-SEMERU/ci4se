def norm(self, x):
    if x not in self:
        raise LinearSpaceTypeError('`x` {!r} is not an element of {!r}'.
            format(x, self))
    return float(self._norm(x))