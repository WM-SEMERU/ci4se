def _recurse_replace(obj, key, new_key, sub, remove):
    if isinstance(obj, list):
        return [_recurse_replace(x, key, new_key, sub, remove) for x in obj]
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            if k == key and v in sub:
                obj[new_key] = sub[v]
                if remove:
                    del obj[key]
            else:
                obj[k] = _recurse_replace(v, key, new_key, sub, remove)
    return obj