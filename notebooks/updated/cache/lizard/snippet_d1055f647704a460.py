def smtp_options(self):
    o = {}
    options = self.options
    for key in self._default_smtp_options:
        if key in options:
            o[key] = options[key]
    o['user'] = o.pop('host_user', None)
    o['password'] = o.pop('host_password', None)
    o['tls'] = o.pop('use_tls', False)
    o['ssl'] = o.pop('use_ssl', False)
    o['debug'] = o.pop('smtp_debug', 0)
    for k in ('certfile', 'keyfile'):
        v = o.pop('ssl_' + k, None)
        if v:
            o[k] = v
    return o