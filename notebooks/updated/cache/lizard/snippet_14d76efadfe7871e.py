def getClassPath():
    global _CLASSPATHS
    global _SEP
    out = []
    for path in _CLASSPATHS:
        if path == '':
            continue
        if path.endswith('*'):
            paths = _glob.glob(path + '.jar')
            if len(path) == 0:
                continue
            out.extend(paths)
        else:
            out.append(path)
    return _SEP.join(out)