def env(key, default=_NOT_PROVIDED, cast=str, force=False, **kwargs):
    boolmap = kwargs.get('boolmap', None)
    sticky = kwargs.get('sticky', False)
    value = os.environ.get(key, default)
    if value is _NOT_PROVIDED:
        raise KeyError(_ENV_ERROR_MSG.format(key))
    if sticky and value == default:
        try:
            os.environ[key] = value
        except TypeError:
            os.environ[key] = str(value)
    if force or value != default and type(value) != cast:
        if cast is bool and boolmap is not None:
            value = boolean(value, boolmap=boolmap)
        elif cast is bool:
            value = boolean(value)
        else:
            value = cast(value)
    return value