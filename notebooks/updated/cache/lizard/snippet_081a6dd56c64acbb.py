def iterstraight(self, raw):
    rb_1 = self.row_bytes + 1
    a = bytearray()
    filt = Filter(self.bitdepth * self.planes)
    for some in raw:
        a.extend(some)
        offset = 0
        while len(a) >= rb_1 + offset:
            filter_type = a[offset]
            if filter_type not in (0, 1, 2, 3, 4):
                raise FormatError(
                    'Invalid PNG Filter Type.  See http://www.w3.org/TR/2003/REC-PNG-20031110/#9Filters .'
                    )
            scanline = a[offset + 1:offset + rb_1]
            filt.undo_filter(filter_type, scanline)
            yield scanline
            offset += rb_1
        del a[:offset]
    if len(a) != 0:
        raise FormatError('Wrong size for decompressed IDAT chunk.')
    assert len(a) == 0