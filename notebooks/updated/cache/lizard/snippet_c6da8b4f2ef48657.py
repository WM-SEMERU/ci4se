def _parse_format(cls, fmt):
    fields = []
    if not fmt:
        raise ValueError('empty format')
    for code, length in fmt:
        if length == 0:
            raise ValueError('zero-length field (bug_compat mismatch?)')
        if code in ('u', 'i') and length in (8, 16, 32, 64
            ) or code == 'f' and length in (32, 64):
            fields.append('>' + code + str(length // 8))
        elif code == 'b' and length == 8:
            fields.append('?')
        elif code == 'c' and length == 8:
            fields.append('S1')
        else:
            if code not in ['u', 'i', 'b']:
                raise ValueError('illegal format ({}, {})'.format(code, length)
                    )
            fields.append('O')
    return _np.dtype(','.join(fields))