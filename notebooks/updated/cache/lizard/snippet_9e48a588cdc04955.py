def top(self, container, ps_args=None):
    u = self._url('/containers/{0}/top', container)
    params = {}
    if ps_args is not None:
        params['ps_args'] = ps_args
    return self._result(self._get(u, params=params), True)