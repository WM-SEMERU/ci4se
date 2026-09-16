def itemComment(self, commentId):
    url = '%s/comments/%s' % (self.root, commentId)
    params = {'f': 'json'}
    return self._get(url, params, securityHandler=self._securityHandler,
        proxy_port=self._proxy_port, proxy_url=self._proxy_url)