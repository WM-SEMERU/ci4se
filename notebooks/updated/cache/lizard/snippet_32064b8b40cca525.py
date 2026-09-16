def discrete(cats, name='discrete'):
    import json
    ks = list(cats)
    for key in ks:
        if isinstance(key, bytes):
            cats[key.decode('utf-8')] = cats.pop(key)
    return 'discrete(' + json.dumps([cats, name]) + ')'