def number(v):
    if nodesetp(v):
        v = string(v)
    try:
        return float(v)
    except ValueError:
        return float('NaN')