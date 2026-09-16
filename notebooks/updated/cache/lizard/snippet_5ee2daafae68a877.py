def urlencode(params):
    if not isinstance(params, dict):
        raise TypeError('Only dicts are supported.')
    params = flatten(params)
    url_params = OrderedDict()
    for param in params:
        value = param.pop()
        name = parametrize(param)
        if isinstance(value, (list, tuple)):
            name += '[]'
        url_params[name] = value
    return urllib_urlencode(url_params, doseq=True)