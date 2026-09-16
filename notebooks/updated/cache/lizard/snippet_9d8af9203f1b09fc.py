def restart(self, container, timeout=10):
    params = {'t': timeout}
    url = self._url('/containers/{0}/restart', container)
    conn_timeout = self.timeout
    if conn_timeout is not None:
        conn_timeout += timeout
    res = self._post(url, params=params, timeout=conn_timeout)
    self._raise_for_status(res)