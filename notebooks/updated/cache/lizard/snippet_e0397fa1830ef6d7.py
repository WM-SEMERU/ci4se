def get_fields_by_prop(cls, prop_key, prop_val):
    ret = []
    for key, val in cls.get_fields_with_prop(prop_key):
        if val == prop_val:
            ret.append(key)
    return ret