def add_env(url, saltenv):
    if not url.startswith('salt://'):
        return url
    path, senv = parse(url)
    return create(path, saltenv)