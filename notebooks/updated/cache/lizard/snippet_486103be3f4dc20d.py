def set_proxy(self, proxy, update=True):
    update_web_driver = False
    if self.current_proxy != proxy:
        update_web_driver = True
    self.current_proxy = proxy
    if proxy is None:
        pass
    else:
        proxy_parts = cutil.get_proxy_parts(proxy)
        if proxy_parts.get('user') is not None:
            self.opts.add_extension(self._proxy_extension(proxy_parts))
        else:
            self.opts.add_argument('--proxy-server={}'.format(proxy))
    if update_web_driver is True:
        self._update()