def unflatten(flat_dict, separator='_'):
    _unflatten_asserts(flat_dict, separator)
    unflattened_dict = dict()

    def _unflatten(dic, keys, value):
        for key in keys[:-1]:
            dic = dic.setdefault(key, {})
        dic[keys[-1]] = value
    for item in flat_dict:
        _unflatten(unflattened_dict, item.split(separator), flat_dict[item])
    return unflattened_dict