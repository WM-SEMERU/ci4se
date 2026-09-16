def assert_free(self, host, port=None):
    if port is None and isinstance(host, abc.Sequence):
        host, port = host[:2]
    if platform.system() == 'Windows':
        host = client_host(host)
    info = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    list(itertools.starmap(self._connect, info))