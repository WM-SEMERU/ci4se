def write_24bit_uint(self, n):
    if type(n) not in python.int_types:
        raise TypeError('expected an int (got:%r)' % (type(n),))
    if not 0 <= n <= 16777215:
        raise OverflowError('n is out of range')
    order = None
    if not self._is_big_endian():
        order = [0, 8, 16]
    else:
        order = [16, 8, 0]
    for x in order:
        self.write_uchar(n >> x & 255)