def is_same_host(self, url):
    if url.startswith('/'):
        return True
    scheme, host, port = get_host(url)
    host = _ipv6_host(host).lower()
    if self.port and not port:
        port = port_by_scheme.get(scheme)
    elif not self.port and port == port_by_scheme.get(scheme):
        port = None
    return (scheme, host, port) == (self.scheme, self.host, self.port)