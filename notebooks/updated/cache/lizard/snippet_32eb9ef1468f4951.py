def read_from_config(cp, **kwargs):
    name = cp.get('model', 'name')
    return models[name].from_config(cp, **kwargs)