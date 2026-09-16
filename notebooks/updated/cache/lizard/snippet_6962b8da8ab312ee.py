def open_connection(func):

    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if kwargs.get('connection', None) is None:
            try:
                host = kwargs.pop('host')
            except KeyError:
                raise TypeError(
                    'one of `connection` or `host` is required to query NDS2 server'
                    )
            kwargs['connection'] = auth_connect(host, kwargs.pop('port', None))
        return func(*args, **kwargs)
    return wrapped_func