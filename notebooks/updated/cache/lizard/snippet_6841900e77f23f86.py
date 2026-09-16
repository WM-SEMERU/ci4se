def default_strlen(strlen=None):
    if strlen is not None:
        _default_types_status['default_strlen'] = strlen
        lstring_as_obj(_default_types_status['lstring_as_obj'])
        ilwd_as_int(_default_types_status['ilwd_as_int'])
    return _default_types_status['default_strlen']