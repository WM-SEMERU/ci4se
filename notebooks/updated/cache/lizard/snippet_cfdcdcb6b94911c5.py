def cmp_dict(d1, d2, ignore_keys=[]):
    return {k: v for k, v in d1.items() if k not in ignore_keys} == {k: v for
        k, v in d2.items() if k not in ignore_keys}