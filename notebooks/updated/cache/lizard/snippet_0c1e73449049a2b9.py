def between(value, prefix, suffix, start=0):
    value = toString(value)
    if prefix == None:
        e = value.find(suffix, start)
        if e == -1:
            return None
        else:
            return value[:e]
    s = value.find(prefix, start)
    if s == -1:
        return None
    s += len(prefix)
    e = value.find(suffix, s)
    if e == -1:
        return None
    s = value.rfind(prefix, start, e) + len(prefix)
    return value[s:e]