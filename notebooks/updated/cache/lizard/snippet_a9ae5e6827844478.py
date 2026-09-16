def select_address_family(host, port):
    if host.startswith('unix://'):
        return socket.AF_UNIX
    elif ':' in host and hasattr(socket, 'AF_INET6'):
        return socket.AF_INET6
    return socket.AF_INET