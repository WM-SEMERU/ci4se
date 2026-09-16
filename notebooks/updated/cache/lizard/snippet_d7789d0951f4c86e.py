def verify_login(user, password=None, **connection_args):
    connection_args['connection_user'] = user
    connection_args['connection_pass'] = password
    dbc = _connect(**connection_args)
    if dbc is None:
        if 'mysql.error' in __context__:
            del __context__['mysql.error']
        return False
    return True