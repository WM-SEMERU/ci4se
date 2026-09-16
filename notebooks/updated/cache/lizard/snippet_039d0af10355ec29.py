def norm_path(path, allow_trailing=True):
    path = _path_re.sub('/', path)
    if path[0] != '/':
        path = '/' + path
    if not allow_trailing and path[-1] == '/':
        path = path[:-1]
    return path