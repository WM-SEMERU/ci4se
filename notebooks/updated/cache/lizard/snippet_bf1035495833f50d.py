def distance_to(self, other):
    other_coord = self._arith_check(other)
    return math.sqrt(math.pow(self._x - other_coord._x, 2) + math.pow(self.
        _y - other_coord._y, 2))