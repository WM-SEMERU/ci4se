def option(self, url, headers=None, kwargs=None):
    return self._request(method='option', url=url, headers=headers, kwargs=
        kwargs)