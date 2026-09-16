def _archive_single_dir(archive):
    common_root = None
    for info in _list_archive_members(archive):
        fn = _info_name(info)
        if fn in set(['.', '/']):
            continue
        sep = None
        if '/' in fn:
            sep = '/'
        elif '\\' in fn:
            sep = '\\'
        if sep is None:
            root_dir = fn
        else:
            root_dir, _ = fn.split(sep, 1)
        if common_root is None:
            common_root = root_dir
        elif common_root != root_dir:
            return None
    return common_root