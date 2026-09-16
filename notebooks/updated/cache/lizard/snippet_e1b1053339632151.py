def _get_frdata(stream, num, name, ctype=None):
    ctypes = (ctype,) if ctype else ('adc', 'proc', 'sim')
    for ctype in ctypes:
        _reader = getattr(stream, 'ReadFr{0}Data'.format(ctype.title()))
        try:
            return _reader(num, name)
        except IndexError as exc:
            if FRERR_NO_CHANNEL_OF_TYPE.match(str(exc)):
                continue
            raise
    raise ValueError('no Fr{{Adc,Proc,Sim}}Data structures with the name {0}'
        .format(name))