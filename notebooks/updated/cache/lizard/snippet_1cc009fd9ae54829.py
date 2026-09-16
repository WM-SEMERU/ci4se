def _parse_parameters(self, resource, params):
    parsed_uri = urlparse(resource)
    qs = parsed_uri.query
    resource = urlunparse(parsed_uri._replace(query=''))
    prms = {}
    for tup in parse_qsl(qs):
        prms[tup[0]] = tup[1]
    for key in params:
        prms[key] = params[key]
    return resource, prms