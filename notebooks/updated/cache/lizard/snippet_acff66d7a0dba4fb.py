def multiply(self, p, e):
    if self._order:
        e %= self._order
    if p == self._infinity or e == 0:
        return self._infinity
    e3 = 3 * e
    i = _leftmost_bit(e3) >> 1
    result = p
    while i > 1:
        result += result
        if e3 & i:
            v = [result, result + p]
        else:
            v = [result - p, result]
        result = v[0 if e & i else 1]
        i >>= 1
    return result