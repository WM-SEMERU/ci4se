def object_merge(old, new, unique=False):
    if isinstance(old, list) and isinstance(new, list):
        if old == new:
            return
        for item in old[::-1]:
            if unique and item in new:
                continue
            new.insert(0, item)
    if isinstance(old, dict) and isinstance(new, dict):
        for key, value in old.items():
            if key not in new:
                new[key] = value
            else:
                object_merge(value, new[key])