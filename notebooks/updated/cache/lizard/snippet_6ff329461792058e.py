def getVersion(data):
    data = data.splitlines()
    return next(v for v, u in zip(data, data[1:]) if len(v) == len(u) and
        allSame(u) and hasDigit(v) and '.' in v)