def mark_path(path):
    if not isinstance(path, str) or os.path.isabs(path):
        msg = 'Error (2D9ZA): Given path is not relative path: {0}.'.format(
            path)
        raise ValueError(msg)
    return _ItemWrapper(type='path', item=path)