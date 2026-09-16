def _get_diffs(cls, dict1, dict2, ignore_missing_keys):
    ret_dict = {}
    for p in dict1.keys():
        if p not in dict2:
            ret_dict.update({p: {'new': dict1[p], 'old': cls.NONE_VALUE}})
        elif dict1[p] != dict2[p]:
            if isinstance(dict1[p], dict) and isinstance(dict2[p], dict):
                sub_diff_dict = cls._get_diffs(dict1[p], dict2[p],
                    ignore_missing_keys)
                if sub_diff_dict:
                    ret_dict.update({p: sub_diff_dict})
            else:
                ret_dict.update({p: {'new': dict1[p], 'old': dict2[p]}})
    if not ignore_missing_keys:
        for p in dict2.keys():
            if p not in dict1.keys():
                ret_dict.update({p: {'new': cls.NONE_VALUE, 'old': dict2[p]}})
    return ret_dict