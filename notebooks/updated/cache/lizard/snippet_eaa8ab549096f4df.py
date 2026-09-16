def get_uri_name(url):
    url_parsed = urlparse(url)
    url_parts = url_parsed.path.split('/')
    log.info('url parts: %s', url_parts)
    return url_parts[-1]