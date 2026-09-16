def _hashes_match(self, a, b):
    if len(a) != len(b):
        return False
    diff = 0
    if six.PY2:
        a = bytearray(a)
        b = bytearray(b)
    for x, y in zip(a, b):
        diff |= x ^ y
    return not diff