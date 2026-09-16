def _fromfile(self):
    self._fd.seek(0)
    try:
        self.byte_order = {b'II': '<', b'MM': '>'}[self._fd.read(2)]
    except KeyError:
        raise ValueError('not a valid TIFF file')
    version = struct.unpack(self.byte_order + 'H', self._fd.read(2))[0]
    if version == 43:
        self.offset_size, zero = struct.unpack(self.byte_order + 'HH', self
            ._fd.read(4))
        if zero or self.offset_size != 8:
            raise ValueError('not a valid BigTIFF file')
    elif version == 42:
        self.offset_size = 4
    else:
        raise ValueError('not a TIFF file')
    self.pages = []
    while True:
        try:
            page = TIFFpage(self)
            self.pages.append(page)
        except StopIteration:
            break
    if not self.pages:
        raise ValueError('empty TIFF file')