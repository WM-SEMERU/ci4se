def _cim_property_value(key, value):
    if key is None:
        raise ValueError('Property name must not be None')
    if isinstance(value, CIMProperty):
        if value.name.lower() != key.lower():
            raise ValueError(_format(
                'CIMProperty.name must be dictionary key {0!A}, but is{1!A}',
                key, value.name))
        prop = value
    else:
        prop = CIMProperty(key, value)
    return prop