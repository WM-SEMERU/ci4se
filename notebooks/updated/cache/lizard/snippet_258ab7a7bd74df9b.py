def zcard(key, host=None, port=None, db=None, password=None):
    server = _connect(host, port, db, password)
    return server.zcard(key)