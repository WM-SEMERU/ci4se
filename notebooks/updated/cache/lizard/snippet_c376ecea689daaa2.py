def cast(type_name, value, **opts):
    type_name, opts = _field_options(type_name, opts)
    return converter(type_name).cast(value, **opts)