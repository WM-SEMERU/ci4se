def get_by_path(path, _globals=None):
    if _globals is None:
        _globals = list()
    return _get_by_path(path.split('.'), _globals)