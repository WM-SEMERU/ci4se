def filter_values(d, vals=None, list_of_dicts=False, deepcopy=True):
    vals = [] if vals is None else vals
    list_of_dicts = '__list__' if list_of_dicts else None
    flatd = flatten(d, list_of_dicts=list_of_dicts)

    def is_in(a, b):
        try:
            return a in b
        except Exception:
            return False
    flatd = {k: v for k, v in flatd.items() if is_in(v, vals)}
    return unflatten(flatd, list_of_dicts=list_of_dicts, deepcopy=deepcopy)