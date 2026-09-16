def addRating(self, rating=5.0):
    if rating > 5.0:
        rating = 5.0
    elif rating < 1.0:
        rating = 1.0
    url = '%s/addRating' % self.root
    params = {'f': 'json', 'rating': '%s' % rating}
    return self._post(url, params, proxy_port=self._proxy_port,
        securityHandler=self._securityHandler, proxy_url=self._proxy_url)