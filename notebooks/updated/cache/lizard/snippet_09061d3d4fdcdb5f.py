def norm_proj_path(path, build_module):
    if path == '//':
        return ''
    if path.startswith('//'):
        norm = normpath(path[2:])
        if norm[0] in ('.', '/', '\\'):
            raise ValueError("Invalid path: `{}'".format(path))
        return norm
    if path.startswith('/'):
        raise ValueError(
            "Invalid path: `{}' - use '//' to start from project root".
            format(path))
    if build_module == '//':
        build_module = ''
    norm = normpath(join(build_module, path))
    if norm.startswith('..'):
        raise ValueError(
            "Invalid path `{}' - must remain inside project sandbox".format
            (path))
    return norm.strip('.')