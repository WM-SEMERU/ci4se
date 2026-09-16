def make_mreq(family, address):
    if not address:
        raise ValueError('Empty address')
    group_bin = pton(family, address)
    if family == socket.AF_INET:
        return group_bin + struct.pack('=I', socket.INADDR_ANY)
    elif family == socket.AF_INET6:
        return group_bin + struct.pack('@I', 0)
    raise ValueError('Unknown family {0}'.format(family))