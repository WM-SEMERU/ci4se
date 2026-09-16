def getfield(f):
    if isinstance(f, list):
        return [getfield(x) for x in f]
    else:
        return f.value