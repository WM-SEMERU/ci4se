def _restore_pmap_field_pickle(key_type, value_type, data):
    type_ = _pmap_field_types[key_type, value_type]
    return _restore_pickle(type_, data)