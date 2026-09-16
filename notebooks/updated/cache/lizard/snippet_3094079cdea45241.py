def build(self, endpoint, values=None, method=None, force_external=False,
    append_unknown=True):
    self.map.update()
    if values:
        if isinstance(values, MultiDict):
            valueiter = values.iteritems(multi=True)
        else:
            valueiter = iteritems(values)
        values = dict((k, v) for k, v in valueiter if v is not None)
    else:
        values = {}
    rv = self._partial_build(endpoint, values, method, append_unknown)
    if rv is None:
        raise BuildError(endpoint, values, method)
    domain_part, path = rv
    host = self.get_host(domain_part)
    if not force_external and (self.map.host_matching and host == self.
        server_name or not self.map.host_matching and domain_part == self.
        subdomain):
        return str(urljoin(self.script_name, './' + path.lstrip('/')))
    return str('%s://%s%s/%s' % (self.url_scheme, host, self.script_name[:-
        1], path.lstrip('/')))