def _split_line(s, parts):
    out = {}
    start = 0
    for name, length in parts:
        out[name] = s[start:start + length].strip()
        start += length
    del out['_']
    return out