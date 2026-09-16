def parse(url):
    config = {}
    url = urlparse.urlparse(url)
    path = url.path[1:]
    path = path.split('?', 2)[0]
    try:
        port = url.port
        hostname = url.hostname
    except ValueError:
        port = None
        if url.scheme == 'rdbms':
            config['INSTANCE'] = url.netloc.split('@')[-1]
            hostname = None
        else:
            hostname = '/cloudsql/{}'.format(url.netloc.split('@')[-1])
    config.update({'NAME': path, 'USER': url.username, 'PASSWORD': url.
        password, 'HOST': hostname, 'PORT': port})
    if url.scheme in SCHEMES:
        config['ENGINE'] = SCHEMES[url.scheme]
    return config