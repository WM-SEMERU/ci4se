def _deep_merge_dict(a, b):
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict):
            _deep_merge_dict(a[k], v)
        else:
            a[k] = v