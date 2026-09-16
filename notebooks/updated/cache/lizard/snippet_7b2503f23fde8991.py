def bind(self, server_name, script_name=None, subdomain=None, url_scheme=
    'http', default_method='GET', path_info=None, query_args=None):
    server_name = server_name.lower()
    if self.host_matching:
        if subdomain is not None:
            raise RuntimeError(
                'host matching enabled and a subdomain was provided')
    elif subdomain is None:
        subdomain = self.default_subdomain
    if script_name is None:
        script_name = '/'
    if path_info is None:
        path_info = '/'
    try:
        server_name = _encode_idna(server_name)
    except UnicodeError:
        raise BadHost()
    return MapAdapter(self, server_name, script_name, subdomain, url_scheme,
        path_info, default_method, query_args)