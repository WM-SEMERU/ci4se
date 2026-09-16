def host_domains(self, ip=None, limit=None, **kwargs):
    return self._results('reverse-ip', '/v1/{0}/host-domains'.format(ip),
        limit=limit, **kwargs)