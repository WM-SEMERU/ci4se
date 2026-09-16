def FeatureContent(self):
    return FeatureContent(url='%s/%s' % (self.root, 'features'),
        securityHandler=self._securityHandler, proxy_url=self._proxy_url,
        proxy_port=self._proxy_port)