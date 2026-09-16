def get_domain_name(url):
    if not url.startswith('http'):
        url = 'http://' + url
    if not is_valid_url(url):
        raise ValueError("Invalid URL '%s'" % url)
    parse = urlparse(url)
    return parse.netloc