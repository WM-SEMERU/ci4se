def force_string(val=None):
    if val is None:
        return ''
    if isinstance(val, list):
        newval = [str(x) for x in val]
        return ';'.join(newval)
    if isinstance(val, str):
        return val
    else:
        return str(val)