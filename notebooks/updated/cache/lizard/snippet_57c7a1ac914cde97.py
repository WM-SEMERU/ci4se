def in6_isaddrTeredo(x):
    our = inet_pton(socket.AF_INET6, x)[0:4]
    teredoPrefix = inet_pton(socket.AF_INET6, conf.teredoPrefix)[0:4]
    return teredoPrefix == our