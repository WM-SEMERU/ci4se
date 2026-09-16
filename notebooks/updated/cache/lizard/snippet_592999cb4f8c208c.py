def is_reachable_host(entity_name):
    try:
        assert type(socket.getaddrinfo(entity_name, 0, 0, 0, 0)) == list
        ret = True
    except socket.gaierror:
        ret = False
    return ret