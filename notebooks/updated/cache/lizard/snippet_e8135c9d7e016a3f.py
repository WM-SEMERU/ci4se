def one_or_more(e, delimiter=None):
    if delimiter is None:
        delimiter = lambda s, grm, pos: (s, Ignore, (pos, pos))
    msg = 'Expected one or more of: {}'.format(repr(e))

    def match_one_or_more(s, grm=None, pos=0):
        start = pos
        s, obj, span = e(s, grm, pos)
        pos = span[1]
        data = [] if obj is Ignore else [obj]
        try:
            while True:
                s, obj, span = delimiter(s, grm, pos)
                pos = span[1]
                if obj is not Ignore:
                    data.append(obj)
                s, obj, span = e(s, grm, pos)
                pos = span[1]
                if obj is not Ignore:
                    data.append(obj)
        except PegreError:
            pass
        return PegreResult(s, data, (start, pos))
    return match_one_or_more