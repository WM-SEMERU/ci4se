def dict_strict_update(base_dict, update_dict):
    additional_keys = set(update_dict.keys()) - set(base_dict.keys())
    if len(additional_keys) > 0:
        raise RuntimeError(
            'The update dictionary contains keys that are not part of the base dictionary: {}'
            .format(str(additional_keys)), additional_keys)
    base_dict.update(update_dict)