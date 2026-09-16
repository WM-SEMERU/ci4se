def as_json(data, **kwargs):
    if 'sort_keys' not in kwargs:
        kwargs['sort_keys'] = False
    if 'ensure_ascii' not in kwargs:
        kwargs['ensure_ascii'] = False
    data = json.dumps(data, **kwargs)
    return data