def dict_merge(dct, merge_dct):
    for key in merge_dct.keys():
        if key in dct and isinstance(dct[key], dict) and isinstance(merge_dct
            [key], collections.Mapping):
            dict_merge(dct[key], merge_dct[key])
        else:
            dct[key] = merge_dct[key]