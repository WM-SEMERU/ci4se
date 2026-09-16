def _expand_host(self, host):
    if isinstance(host, basestring):
        return host, self.default_port
    return tuple(host)