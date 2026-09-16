def safe_serialize_type(l):
    if isinstance(l, str):
        return l
    elif isinstance(l, list):
        return '%s_%s_' % (l[0], ''.join(map(safe_serialize_type, l[1:])))
    else:
        return str(l)