def list(path, filename=None, start=None, stop=None, recursive=False,
    directories=False):
    path = uri_to_path(path)
    if not filename and recursive:
        return listrecursive(path)
    if filename:
        if os.path.isdir(path):
            path = os.path.join(path, filename)
        else:
            path = os.path.join(os.path.dirname(path), filename)
    elif os.path.isdir(path) and not directories:
        path = os.path.join(path, '*')
    files = glob.glob(path)
    if not directories:
        files = [fpath for fpath in files if not os.path.isdir(fpath)]
    files.sort()
    files = select(files, start, stop)
    return files