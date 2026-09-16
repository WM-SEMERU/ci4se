def list_of_lists_to_dict(l):
    d = {}
    for key, val in l:
        d.setdefault(key, []).append(val)
    return d