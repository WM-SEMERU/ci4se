def create_archiver(typename):
    archiver = _ARCHIVER_BY_TYPE.get(typename)
    if not archiver:
        raise ValueError('No archiver registered for {!r}'.format(typename))
    return archiver