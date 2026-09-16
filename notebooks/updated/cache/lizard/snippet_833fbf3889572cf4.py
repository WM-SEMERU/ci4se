def _create_dict_with_nested_keys_and_val(cls, keys, value):
    if len(keys) > 1:
        new_keys = keys[:-1]
        new_val = {keys[-1]: value}
        return cls._create_dict_with_nested_keys_and_val(new_keys, new_val)
    elif len(keys) == 1:
        return {keys[0]: value}
    else:
        raise ValueError('Keys must contain at least one key.')