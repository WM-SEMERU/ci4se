def urljoin(domain, path=None, scheme=None):
    if scheme is None:
        scheme = getattr(settings, 'DEFAULT_URL_SCHEME', 'http')
    return urlunparse((scheme, domain, path or '', None, None, None))