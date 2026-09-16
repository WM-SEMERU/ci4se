def walk(pathobj, topdown=True):
    dirs, nondirs = [], []
    for child in pathobj:
        relpath = str(child.relative_to(str(pathobj)))
        if relpath.startswith('/'):
            relpath = relpath[1:]
        if relpath.endswith('/'):
            relpath = relpath[:-1]
        if child.is_dir():
            dirs.append(relpath)
        else:
            nondirs.append(relpath)
    if topdown:
        yield pathobj, dirs, nondirs
    for dir in dirs:
        for result in walk(pathobj / dir):
            yield result
    if not topdown:
        yield pathobj, dirs, nondirs