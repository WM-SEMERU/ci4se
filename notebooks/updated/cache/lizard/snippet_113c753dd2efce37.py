def _send(self, **req_kwargs):
    auth_token = self._auth.getAuthToken()
    if auth_token is None:
        raise exception.LoginException('Not logged in')
    req_kwargs.setdefault('headers', {'Authorization': 'OAuth ' + auth_token})
    return self._session.request(**req_kwargs)