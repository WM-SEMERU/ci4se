def getRelativePath(basepath, path):
    basepath = splitpath(os.path.abspath(basepath))
    path = splitpath(os.path.abspath(path))
    afterCommon = False
    for c in basepath:
        if afterCommon or path[0] != c:
            path.insert(0, os.path.pardir)
            afterCommon = True
        else:
            del path[0]
    return os.path.join(*path)