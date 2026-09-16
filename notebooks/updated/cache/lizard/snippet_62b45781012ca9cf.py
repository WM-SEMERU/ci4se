def _list_merge(src, dest):
    for k in src:
        if type(src[k]) != dict:
            dest[k] = src[k]
        else:
            if k not in dest:
                dest[k] = {}
            _list_merge(src[k], dest[k])