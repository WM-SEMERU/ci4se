def _config(name, key=None, **kwargs):
    if key is None:
        key = name
    if name in kwargs:
        value = kwargs[name]
    else:
        value = __salt__['config.option']('ddns.{0}'.format(key))
        if not value:
            value = None
    return value