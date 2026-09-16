def _flatten_dicts(self, dicts):
    d = dict()
    list_of_dicts = [d.get() for d in dicts or []]
    return {k: v for d in list_of_dicts for k, v in d.items()}