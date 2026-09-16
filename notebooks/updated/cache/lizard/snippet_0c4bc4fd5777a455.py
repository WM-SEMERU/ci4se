def fromvalue(self, value, size=None, fmt='Q'):
    if size and value.bit_length() > size:
        raise TypeError('Value is too big for given size')
    self.frombytes(struct.pack(fmt, value))
    if size:
        if not isinstance(size, integer_types) or not size > 0:
            raise TypeError('Size must be greater than zero')
        if size > self.length():
            bitarray.extend(self, (size - self.length()) * [0])
        else:
            bitarray.__delitem__(self, slice(size, self.length()))