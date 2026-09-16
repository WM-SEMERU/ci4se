def cache_dir(path, saltenv='base', include_empty=False, include_pat=None,
    exclude_pat=None):
    return _client().cache_dir(path, saltenv, include_empty, include_pat,
        exclude_pat)