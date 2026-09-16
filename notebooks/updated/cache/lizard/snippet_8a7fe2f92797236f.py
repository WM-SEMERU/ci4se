def add_to_capabilities(self, capabilities):
    proxy_caps = {}
    proxy_caps['proxyType'] = self.proxyType['string']
    if self.autodetect:
        proxy_caps['autodetect'] = self.autodetect
    if self.ftpProxy:
        proxy_caps['ftpProxy'] = self.ftpProxy
    if self.httpProxy:
        proxy_caps['httpProxy'] = self.httpProxy
    if self.proxyAutoconfigUrl:
        proxy_caps['proxyAutoconfigUrl'] = self.proxyAutoconfigUrl
    if self.sslProxy:
        proxy_caps['sslProxy'] = self.sslProxy
    if self.noProxy:
        proxy_caps['noProxy'] = self.noProxy
    if self.socksProxy:
        proxy_caps['socksProxy'] = self.socksProxy
    if self.socksUsername:
        proxy_caps['socksUsername'] = self.socksUsername
    if self.socksPassword:
        proxy_caps['socksPassword'] = self.socksPassword
    capabilities['proxy'] = proxy_caps