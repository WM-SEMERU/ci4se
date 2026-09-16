def _join_factory(cls, gap, pad):
    if issubclass(cls, dict):

        def _join(data):
            out = cls()
            data = list(data)
            while data:
                tsd = data.pop(0)
                out.append(tsd, gap=gap, pad=pad)
                del tsd
            return out
    else:
        from .. import TimeSeriesBaseList

        def _join(arrays):
            list_ = TimeSeriesBaseList(*arrays)
            return list_.join(pad=pad, gap=gap)
    return _join