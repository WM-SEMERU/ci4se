def item_to_mrc(code, val):
    if isinstance(val, basestring):
        return [val_to_mrc(code, val)]
    if isinstance(val, dict):
        val = [val]
    return dicts_to_mrc(code, val)