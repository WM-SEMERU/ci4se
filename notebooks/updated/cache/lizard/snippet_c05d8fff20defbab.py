def ida_connect(host='localhost', port=18861, retry=10):
    for i in range(retry):
        try:
            LOG.debug('Connectint to %s:%d, try %d...', host, port, i + 1)
            link = rpyc_classic.connect(host, port)
            link.eval('2 + 2')
        except socket.error:
            time.sleep(1)
            continue
        else:
            LOG.debug('Connected to %s:%d', host, port)
            return link
    raise IDALinkError('Could not connect to %s:%d after %d tries' % (host,
        port, retry))