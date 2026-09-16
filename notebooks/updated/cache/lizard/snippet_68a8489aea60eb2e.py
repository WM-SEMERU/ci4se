def build_url(base_url, partial_url):
    if not base_url.endswith('/'):
        base_url += '/'
    if partial_url.startswith('/'):
        partial_url = partial_url[1:]
    return urlparse.urljoin(base_url, partial_url)