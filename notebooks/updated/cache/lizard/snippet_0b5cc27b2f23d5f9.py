def _choose_pool(self, protocol=None):
    if not protocol:
        protocol = self.protocol
    if protocol == 'http':
        pool = self._http_pool
    elif protocol == 'tcp' or protocol == 'pbc':
        pool = self._tcp_pool
    else:
        raise ValueError('invalid protocol %s' % protocol)
    if pool is None or self._closed:
        raise RuntimeError('Client is closed.')
    return pool