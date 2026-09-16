def _get_path(dict_, path):
    cur = dict_
    for part in path.split('/'):
        cur = cur[part]
    return cur