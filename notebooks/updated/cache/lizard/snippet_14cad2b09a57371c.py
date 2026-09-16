def param(name, help=''):

    def decorator(func):
        params = getattr(func, 'params', [])
        _param = Param(name, help)
        params.insert(0, _param)
        func.params = params
        return func
    return decorator