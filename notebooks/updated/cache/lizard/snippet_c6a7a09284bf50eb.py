def read_csv(fname, sep=','):
    with open(fname, encoding='utf-8-sig') as f:
        header = next(f).strip().split(sep)
        dt = numpy.dtype([(h, numpy.bool if h == 'vs30measured' else float) for
            h in header])
        return numpy.loadtxt(f, dt, delimiter=sep)