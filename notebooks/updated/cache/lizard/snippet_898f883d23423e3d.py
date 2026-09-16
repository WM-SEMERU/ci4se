def exec_resize(self, exec_id, height=None, width=None):
    if isinstance(exec_id, dict):
        exec_id = exec_id.get('Id')
    params = {'h': height, 'w': width}
    url = self._url('/exec/{0}/resize', exec_id)
    res = self._post(url, params=params)
    self._raise_for_status(res)