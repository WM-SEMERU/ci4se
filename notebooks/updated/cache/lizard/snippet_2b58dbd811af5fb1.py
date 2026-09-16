def get_choices(cls, category):
    value = cls._DEFAULTS[category]
    if not isinstance(value, list):
        raise ValueError('{} does not offer choices'.format(category))
    return value