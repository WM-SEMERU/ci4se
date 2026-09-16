def list_patterns(refresh=False, root=None):
    if refresh:
        refresh_db(root)
    return _get_patterns(root=root)