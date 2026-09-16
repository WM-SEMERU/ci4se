def tee(data, n=2):
    if isinstance(data, (Stream, Iterator)):
        return tuple(Stream(cp) for cp in it.tee(data, n))
    else:
        return tuple(data for unused in xrange(n))