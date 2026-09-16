def _do_get(self, uri, **kwargs):
    scaleioapi_get_headers = {'Content-type': 'application/json', 'Version':
        '1.0'}
    self.logger.debug('_do_get() ' + '{}/{}'.format(self._api_url, uri))
    if kwargs:
        for key, value in kwargs.iteritems():
            if key == 'headers':
                scaleio_get_headersvalue = value
    try:
        response = self._im_session.get('{}/{}'.format(self._api_url, uri),
            **kwargs).json()
        if response.status_code == requests.codes.ok:
            return response
        else:
            raise RuntimeError('_do_get() - HTTP response error' + response
                .status_code)
    except:
        raise RuntimeError(
            '_do_get() - Communication error with ScaleIO gateway')
    return response