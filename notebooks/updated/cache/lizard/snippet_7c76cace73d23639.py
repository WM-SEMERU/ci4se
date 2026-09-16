def iterdata(fd, close_fd=True, **opts):
    fmt = opts.get('format', 'lines')
    fopts = fmtopts.get(fmt, {})
    for opt, val in fopts.items():
        opts.setdefault(opt, val)
    ncod = opts.get('encoding')
    if ncod is not None:
        fd = codecs.getreader(ncod)(fd)
    fmtr = fmtyielders.get(fmt)
    if fmtr is None:
        raise s_exc.NoSuchImpl(name=fmt, knowns=fmtyielders.keys())
    for item in fmtr(fd, opts):
        yield item
    if close_fd:
        fd.close()