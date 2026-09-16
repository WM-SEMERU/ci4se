def filter(func, data):
    out = []
    for r in data:
        if func(r):
            out.append(r)
    return out