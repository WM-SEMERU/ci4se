def _request(self, method, url, headers=None, body=None, kwargs=None):
    _kwargs = utils.dict_update(self.request_kwargs.copy(), kwargs)
    _headers = utils.dict_update(self.headers.copy(), headers)
    _url = self._get_url(url=url)
    try:
        func = getattr(requests, method.lower())
        if body is None:
            resp = func(_url, headers=_headers, **_kwargs)
        else:
            resp = func(_url, data=body, headers=_headers, **_kwargs)
        self.log.debug('%s %s %s', resp.status_code, resp.reason, resp.request)
    except AttributeError as exp:
        self._report_error(request=method.upper(), exp=exp)
    else:
        return resp