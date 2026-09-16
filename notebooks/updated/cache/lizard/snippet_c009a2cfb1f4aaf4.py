def get_fields_with_prop(cls, prop_key):
    ret = []
    for key, val in getattr(cls, '_fields').items():
        if hasattr(val, prop_key):
            ret.append((key, getattr(val, prop_key)))
    return ret