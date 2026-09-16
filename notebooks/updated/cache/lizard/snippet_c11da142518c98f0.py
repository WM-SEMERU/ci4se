def _property_create_dict(header, data):
    prop = dict(zip(header, _merge_last(data, len(header))))
    prop['name'] = _property_normalize_name(prop['property'])
    prop['type'] = _property_detect_type(prop['name'], prop['values'])
    prop['edit'] = from_bool(prop['edit'])
    if 'inherit' in prop:
        prop['inherit'] = from_bool(prop['inherit'])
    del prop['property']
    return prop