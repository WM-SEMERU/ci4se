def _make_request(self, action):
    if isinstance(action, list):
        kwargs = {'actions': action}
        action = 'send'
    else:
        kwargs = self._get_method_params()
    kwargs.update({'consumer_key': self._consumer_key, 'access_token': self
        ._access_token})
    response = requests.post(self._get_url(action), json=kwargs, headers=
        self._get_headers())
    if response.status_code != requests.codes.ok:
        raise self._make_exception(response)
    return response.json()