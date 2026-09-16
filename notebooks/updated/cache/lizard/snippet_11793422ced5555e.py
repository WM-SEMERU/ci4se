def parse_qsl(qs, keep_blank_values=0, strict_parsing=0):
    pairs = []
    name_value_amp = qs.split('&')
    for name_value in name_value_amp:
        if ';' in name_value:
            pairs.extend([x, ';'] for x in name_value.split(';'))
            pairs[-1][1] = '&'
        else:
            pairs.append([name_value, '&'])
    pairs[-1][1] = ''
    r = []
    for name_value, sep in pairs:
        nv = name_value.split('=', 1)
        if len(nv) != 2:
            if strict_parsing:
                raise ValueError('bad query field: %r' % name_value)
            elif len(nv) == 1:
                nv = nv[0], None
            else:
                continue
        if nv[1] or keep_blank_values:
            name = urllib.unquote(nv[0].replace('+', ' '))
            if nv[1]:
                value = urllib.unquote(nv[1].replace('+', ' '))
            else:
                value = nv[1]
            r.append((name, value, sep))
    return r