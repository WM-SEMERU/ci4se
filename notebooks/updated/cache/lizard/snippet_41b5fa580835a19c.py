def get(name, import_str=False):
    value = None
    default_value = getattr(default_settings, name)
    try:
        value = getattr(settings, name)
    except AttributeError:
        if name in default_settings.required_attrs:
            raise Exception('You must set ' + name + ' in your settings.')
    if isinstance(default_value, dict) and value:
        default_value.update(value)
        value = default_value
    else:
        if value is None:
            value = default_value
        value = import_from_str(value) if import_str else value
    return value