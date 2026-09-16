def _eq_dicts(d1, d2):
    if not d1.keys() == d2.keys():
        return False
    for k, v1 in d1.items():
        v2 = d2[k]
        if not type(v1) == type(v2):
            return False
        if isinstance(v1, np.ndarray):
            if not np.array_equal(v1, v2):
                return False
        elif not v1 == v2:
            return False
    return True