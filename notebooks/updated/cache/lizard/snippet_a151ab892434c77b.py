def filter_keys(d, keys, use_wildcards=False, list_of_dicts=False, deepcopy
    =True):
    list_of_dicts = '__list__' if list_of_dicts else None
    flatd = flatten(d, list_of_dicts=list_of_dicts)

    def is_in(a, bs):
        if use_wildcards:
            for b in bs:
                try:
                    if a == b:
                        return True
                    if fnmatch(b, a):
                        return True
                except Exception:
                    pass
            return False
        else:
            try:
                return a in bs
            except Exception:
                return False
    flatd = {paths: v for paths, v in flatd.items() if any([is_in(k, paths) for
        k in keys])}
    return unflatten(flatd, list_of_dicts=list_of_dicts, deepcopy=deepcopy)