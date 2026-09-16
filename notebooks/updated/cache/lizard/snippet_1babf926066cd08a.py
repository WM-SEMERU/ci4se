def build_url(host, path):
    host += '/' if not host.endswith('/') else ''
    path = path.lstrip('/')
    return parse.urljoin(host, path)