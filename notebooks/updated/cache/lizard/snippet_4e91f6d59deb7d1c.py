def get_http_url(url, req, method='GET'):
    if method in ['GET', 'DELETE']:
        if req.keys():
            _req = req.copy()
            comp = urlsplit(str(url))
            if comp.query:
                _req.update(parse_qs(comp.query))
            _query = str(_req.to_urlencoded())
            return urlunsplit((comp.scheme, comp.netloc, comp.path, _query,
                comp.fragment))
        else:
            return url
    else:
        return url