def dicts_equal(d1, d2):
    if len(d1) != len(d2):
        return False
    for k in d1:
        if k not in d2:
            return False
    for k in d2:
        if k not in d1:
            return False
    for k in d1:
        if type(d1[k]) != type(d2[k]):
            return False
        elif isinstance(d1[k], list):
            if not sorted(d1[k]) == sorted(d2[k]):
                return False
        elif isinstance(d1[k], dict):
            if not dicts_equal(d1[k], d2[k]):
                return False
        elif d1[k] != d2[k]:
            return False
    return True