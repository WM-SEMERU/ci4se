def find_mirteFile(name, extra_path=None):
    extra_path = () if extra_path is None else extra_path
    for bp in chain(extra_path, sys.path):
        pb = os.path.join(bp, name)
        p = pb + FILE_SUFFIX
        if os.path.exists(p):
            return os.path.abspath(p)
        p = os.path.join(pb, DEFAULT_FILE)
        if os.path.exists(p):
            return os.path.abspath(p)
    raise ValueError("Couldn't find mirteFile %s" % name)