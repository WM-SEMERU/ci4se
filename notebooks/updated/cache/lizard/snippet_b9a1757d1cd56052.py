def send(self, stream=False):
    try:
        response = self.session.request(self._http_method, self._url, auth=
            self._basic_auth, data=self._body, files=self._files, headers=
            self._headers, params=self._payload, stream=stream, timeout=
            self._timeout)
    except Exception as e:
        err = 'Failed making HTTP request ({}).'.format(e)
        raise RuntimeError(err)
    self.tcex.log.info('Status Code: {}'.format(response.status_code))
    return response