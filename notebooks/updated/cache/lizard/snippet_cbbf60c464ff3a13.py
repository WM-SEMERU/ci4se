def query_dqsegdb(cls, flags, *args, **kwargs):
    on_error = kwargs.pop('on_error', 'raise').lower()
    if on_error not in ['raise', 'warn', 'ignore']:
        raise ValueError("on_error must be one of 'raise', 'warn', or 'ignore'"
            )
    qsegs = _parse_query_segments(args, cls.query_dqsegdb)
    inq = Queue()
    outq = Queue()
    for i in range(len(flags)):
        t = _QueryDQSegDBThread(inq, outq, qsegs, **kwargs)
        t.setDaemon(True)
        t.start()
    for i, flag in enumerate(flags):
        inq.put((i, flag))
    inq.join()
    outq.join()
    new = cls()
    results = list(zip(*sorted([outq.get() for i in range(len(flags))], key
        =lambda x: x[0])))[1]
    for result, flag in zip(results, flags):
        if isinstance(result, Exception):
            result.args = '%s [%s]' % (str(result), str(flag)),
            if on_error == 'ignore':
                pass
            elif on_error == 'warn':
                warnings.warn(str(result))
            else:
                raise result
        else:
            new[flag] = result
    return new