def merge_dicts(*dicts, **copy_check):
    merged = {}
    if not dicts:
        return merged
    for index, merge_dict in enumerate(dicts):
        if index == 0 and not copy_check.get('copy'):
            merged = merge_dict
        else:
            merged.update(merge_dict)
    return merged