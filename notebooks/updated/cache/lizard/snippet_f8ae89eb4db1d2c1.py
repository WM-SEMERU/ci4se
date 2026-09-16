def is_list_like(obj):
    return isinstance(obj, _LIST_LIKE_TYPES) and not (isinstance(obj,
        anyconfig.compat.STR_TYPES) or is_dict_like(obj))