def uploadItem(self, filePath, description):
    import urlparse
    url = self._url + '/upload'
    params = {'f': 'json'}
    files = {}
    files['itemFile'] = filePath
    return self._post(url=url, param_dict=params, files=files,
        securityHandler=self._securityHandler, proxy_url=self._proxy_url,
        proxy_port=self._proxy_port)