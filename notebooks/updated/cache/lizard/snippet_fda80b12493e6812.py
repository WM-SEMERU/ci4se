def _createtoken(self, type_, value, flags=None):
    pos = None
    assert len(self._positions) >= 2, (type_, value)
    p2 = self._positions.pop()
    p1 = self._positions.pop()
    pos = [p1, p2]
    return token(type_, value, pos, flags)