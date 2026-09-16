def _sslobj(sock):
    pass
    if isinstance(sock._sslobj, _ssl._SSLSocket):
        return sock._sslobj
    else:
        return sock._sslobj._sslobj