def rglob(dirname, pattern, dirs=False, sort=True):
    fns = []
    path = str(dirname)
    if os.path.isdir(path):
        fns = glob(os.path.join(escape(path), pattern))
        dns = [fn for fn in [os.path.join(path, fn) for fn in os.listdir(
            path)] if os.path.isdir(fn)]
        if dirs == True:
            fns += dns
        for d in dns:
            fns += rglob(d, pattern)
        if sort == True:
            fns.sort()
    else:
        log.warn('not a directory: %r' % path)
    return fns