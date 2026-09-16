def fromfile(cls, f):
    filter = cls()
    filter._setup(*unpack(cls.FILE_FMT, f.read(calcsize(cls.FILE_FMT))))
    nfilters, = unpack(b'<l', f.read(calcsize(b'<l')))
    if nfilters > 0:
        header_fmt = b'<' + b'Q' * nfilters
        bytes = f.read(calcsize(header_fmt))
        filter_lengths = unpack(header_fmt, bytes)
        for fl in filter_lengths:
            filter.filters.append(BloomFilter.fromfile(f, fl))
    else:
        filter.filters = []
    return filter