def bitcount(self, key, start=None, end=None):
    command = [b'BITCOUNT', key]
    if start is not None and end is None:
        raise ValueError('Can not specify start without an end')
    elif start is None and end is not None:
        raise ValueError('Can not specify start without an end')
    elif start is not None and end is not None:
        command += [ascii(start), ascii(end)]
    return self._execute(command)