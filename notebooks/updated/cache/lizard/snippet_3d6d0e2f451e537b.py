def _build_namespace_dict(cls, obj, dots=False):
    obj = namespace_to_dict(obj)
    if not isinstance(obj, dict):
        return obj
    keys = obj.keys() if PY3 else obj.iterkeys()
    if dots:
        keys = sorted(list(keys))
    output = {}
    for key in keys:
        value = obj[key]
        if value is None:
            continue
        save_to = output
        result = cls._build_namespace_dict(value, dots)
        if dots:
            split = key.split('.')
            if len(split) > 1:
                key = split.pop()
                for child_key in split:
                    if child_key in save_to and isinstance(save_to[
                        child_key], dict):
                        save_to = save_to[child_key]
                    else:
                        save_to[child_key] = {}
                        save_to = save_to[child_key]
        if key in save_to:
            save_to[key].update(result)
        else:
            save_to[key] = result
    return output