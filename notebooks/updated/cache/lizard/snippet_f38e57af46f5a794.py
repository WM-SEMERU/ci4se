def has_pair(ip, alias):
    hosts = _list_hosts()
    try:
        return alias in hosts[ip]
    except KeyError:
        return False