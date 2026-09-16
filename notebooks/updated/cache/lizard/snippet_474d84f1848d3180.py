def xnormpath(path):
    normalized = posixpath.normpath(path).replace(b'\\', b'/')
    return posixpath.normpath(normalized)