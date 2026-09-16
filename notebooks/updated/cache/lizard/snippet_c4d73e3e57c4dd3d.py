def key_value_contents(use_dict=None, as_class=dict, key_values=()):
    if _debug:
        key_value_contents._debug(
            'key_value_contents use_dict=%r as_class=%r key_values=%r',
            use_dict, as_class, key_values)
    if use_dict is None:
        use_dict = as_class()
    for k, v in key_values:
        if v is not None:
            if hasattr(v, 'dict_contents'):
                v = v.dict_contents(as_class=as_class)
            use_dict.__setitem__(k, v)
    return use_dict