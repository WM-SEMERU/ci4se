def saved_search(self, sid, **kw):
    path = 'data/v1/searches/%s/results' % sid
    params = self._params(kw)
    return self._get(self._url(path), body_type=models.Items, params=params
        ).get_body()