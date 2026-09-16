def check_extraneous(config, schema):
    if not isinstance(config, dict):
        raise ValueError('Config {} is not a dictionary'.format(config))
    for k in config:
        if k not in schema:
            raise ValueError('Unexpected config key `{}` not in {}'.format(
                k, list(schema.keys())))
        v, kreq = schema[k]
        if v is None:
            continue
        elif isinstance(v, type):
            if not isinstance(config[k], v):
                if v is str and isinstance(config[k], string_types):
                    continue
                raise ValueError(
                    'Config key `{}` has wrong type {}, expected {}'.format
                    (k, type(config[k]).__name__, v.__name__))
        else:
            check_extraneous(config[k], v)