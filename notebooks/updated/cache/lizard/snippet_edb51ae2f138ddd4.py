def parse_remote_url(url):
    if url.startswith('git@'):
        path = url.split(':', 1)[1]
    else:
        parsed = urllib.parse.urlparse(url)
        path = parsed.path[1:]
    assert path.endswith('.git'), path
    path = path[:-4]
    return path.split('/')