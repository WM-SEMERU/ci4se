def groupselectfirst(table, key, presorted=False, buffersize=None, tempdir=
    None, cache=True):

    def _reducer(k, rows):
        return next(rows)
    return rowreduce(table, key, reducer=_reducer, presorted=presorted,
        buffersize=buffersize, tempdir=tempdir, cache=cache)