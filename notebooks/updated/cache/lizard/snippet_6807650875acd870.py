def copy_attribute_values(source, target, property_names):
    if source is None:
        raise ValueError('"source" must be provided.')
    if target is None:
        raise ValueError('"target" must be provided.')
    if property_names is None:
        raise ValueError('"property_list" must be provided.')
    if not hasattr(property_names, '__iter__') or isinstance(property_names,
        str):
        raise ValueError(
            '"property_names" must be a sequence type, such as list or set.')
    for property_name in property_names:
        if hasattr(source, property_name):
            setattr(target, property_name, getattr(source, property_name))