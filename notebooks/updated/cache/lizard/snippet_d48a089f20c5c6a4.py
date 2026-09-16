def resolve_file(fname, paths):
    fpath = path.abspath(fname)
    for p in paths:
        spath = path.abspath(p)
        if fpath.startswith(spath):
            return fpath[len(spath) + 1:]
    return fname