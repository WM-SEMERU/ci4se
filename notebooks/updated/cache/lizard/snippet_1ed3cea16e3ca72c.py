def merge(d, *dicts):
    for d_update in dicts:
        if not isinstance(d, dict):
            raise TypeError('{0} is not a dict'.format(d))
        dict_merge_pair(d, d_update)
    return d