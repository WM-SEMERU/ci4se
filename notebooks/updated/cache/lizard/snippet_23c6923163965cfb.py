def contains_group(store, path=None):
    path = normalize_storage_path(path)
    prefix = _path_to_prefix(path)
    key = prefix + group_meta_key
    return key in store