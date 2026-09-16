def _set_proxy_headers(self, url, headers=None):
    headers_ = {'Accept': '*/*'}
    netloc = parse_url(url).netloc
    if netloc:
        headers_['Host'] = netloc
    if headers:
        headers_.update(headers)
    return headers_