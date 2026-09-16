def group(self):
    split_count = self._url.lower().find('/content/')
    len_count = len('/content/')
    gURL = self._url[:self._url.lower().find('/content/')
        ] + '/community/' + self._url[split_count + len_count:]
    return CommunityGroup(url=gURL, securityHandler=self._securityHandler,
        proxy_url=self._proxy_url, proxy_port=self._proxy_port)