def normalize_path(path, base_path='/', is_dir=None):
    u
    path = posixpath.normpath(path)
    base_path = posixpath.normpath(base_path)
    if len(base_path) == 0:
        raise ValueError(
            '`project_root` cannot be an empty string after normalization')
    if base_path[-1] != '/':
        base_path += '/'
    if path.startswith(base_path):
        path = '/' + posixpath.relpath(path, base_path)
    elif path.startswith('/'):
        raise ValueError(
            '`path` ({}) is absolute but not inside base_path ({})'.format(
            path, base_path))
    if is_dir is None:
        return path
    elif is_dir and path[-1:] != '/':
        return path + '/'
    elif not is_dir and path[-1:] == '/':
        return path[:-1]
    return path