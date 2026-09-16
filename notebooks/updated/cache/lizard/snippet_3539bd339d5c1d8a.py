def _expand_path(path):
    path = os.path.expandvars(path)
    path = os.path.expanduser(path)
    return path