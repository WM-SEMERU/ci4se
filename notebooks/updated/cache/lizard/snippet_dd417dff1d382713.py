def dump(obj, fp, **kwargs):
    kwargs['default'] = serialize
    return json.dump(obj, fp, **kwargs)