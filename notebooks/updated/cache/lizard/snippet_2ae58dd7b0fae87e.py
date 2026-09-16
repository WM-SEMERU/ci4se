def set_key(key, value, host=None, port=None, db=None, password=None):
    server = _connect(host, port, db, password)
    return server.set(key, value)