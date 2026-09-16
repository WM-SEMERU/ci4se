def mkdtemp(suffix=None, prefix=None, dir=None):
    suffix = fsnative() if suffix is None else path2fsn(suffix)
    prefix = gettempprefix() if prefix is None else path2fsn(prefix)
    dir = gettempdir() if dir is None else path2fsn(dir)
    return tempfile.mkdtemp(suffix, prefix, dir)