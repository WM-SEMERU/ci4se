def _ilshift(self, n):
    assert 0 < n <= self.len
    self._append(Bits(n))
    self._truncatestart(n)
    return self