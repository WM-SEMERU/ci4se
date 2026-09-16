def get_connection(self, url, proxies=None):
    proxies = proxies or {}
    proxy = proxies.get(urlparse(url.lower()).scheme)
    if proxy:
        proxy = prepend_scheme_if_needed(proxy, 'http')
        proxy_manager = self.proxy_manager_for(proxy)
        conn = proxy_manager.connection_from_url(url)
    else:
        parsed = urlparse(url)
        url = parsed.geturl()
        conn = self.poolmanager.connection_from_url(url)
    return conn