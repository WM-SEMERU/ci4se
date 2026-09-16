def get_host(url):
    port = None
    scheme = 'http'
    if '//' in url:
        scheme, url = url.split('://', 1)
    if '/' in url:
        url, _path = url.split('/', 1)
    if ':' in url:
        url, port = url.split(':', 1)
        port = int(port)
    return scheme, url, port