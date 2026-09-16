def hex_repr(d):
    txt = []
    for k, v in sorted(d.items()):
        if isinstance(v, int):
            txt.append('%s=%s' % (k, nice_hex(v)))
        else:
            txt.append('%s=%s' % (k, v))
    return ' '.join(txt)