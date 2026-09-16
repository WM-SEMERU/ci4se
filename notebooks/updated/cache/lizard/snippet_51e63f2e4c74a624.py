def is_bool_list(value, min=None, max=None):
    return [is_boolean(mem) for mem in is_list(value, min, max)]