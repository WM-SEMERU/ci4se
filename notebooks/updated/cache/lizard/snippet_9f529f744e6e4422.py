def _get_url(url):
    if isinstance(url, urlparse.ParseResult):
        return urlparse.urlunparse(url)
    else:
        return url