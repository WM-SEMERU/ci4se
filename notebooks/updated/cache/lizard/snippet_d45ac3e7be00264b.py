def get_fqhostname():
    fqdn = None
    try:
        addrinfo = socket.getaddrinfo(socket.gethostname(), 0, socket.
            AF_UNSPEC, socket.SOCK_STREAM, socket.SOL_TCP, socket.AI_CANONNAME)
        for info in addrinfo:
            if len(info) > 3 and info[3]:
                fqdn = info[3]
                break
    except socket.gaierror:
        pass
    except socket.error as err:
        log.debug('socket.getaddrinfo() failure while finding fqdn: %s', err)
    if fqdn is None:
        fqdn = socket.getfqdn()
    return fqdn