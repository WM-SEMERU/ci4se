def proxy_servers(self):
    proxy_servers = {}
    if self._load_rc_func is None:
        return proxy_servers
    else:
        HTTP_PROXY = os.environ.get('HTTP_PROXY')
        HTTPS_PROXY = os.environ.get('HTTPS_PROXY')
        if HTTP_PROXY:
            proxy_servers['http'] = HTTP_PROXY
        if HTTPS_PROXY:
            proxy_servers['https'] = HTTPS_PROXY
        proxy_servers_conf = self._load_rc_func().get('proxy_servers', {})
        proxy_servers.update(proxy_servers_conf)
        return proxy_servers