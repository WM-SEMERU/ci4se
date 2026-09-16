def call(conn=None, call=None, kwargs=None):
    if call == 'action':
        raise SaltCloudSystemExit(
            'The call function must be called with -f or --function.')
    if 'func' not in kwargs:
        raise SaltCloudSystemExit('No `func` argument passed')
    if conn is None:
        conn = get_conn()
    func = kwargs.pop('func')
    for key, value in kwargs.items():
        try:
            kwargs[key] = __utils__['json.loads'](value)
        except ValueError:
            continue
    try:
        return getattr(conn, func)(**kwargs)
    except shade.exc.OpenStackCloudException as exc:
        log.error('Error running %s: %s', func, exc)
        raise SaltCloudSystemExit(six.text_type(exc))