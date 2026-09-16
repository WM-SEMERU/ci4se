def humanize_api_path(api_path):
    return reduce(lambda val, func: func(val), [parameterize, underscore,
        camelize], unicode(api_path))