def get_login_url(self, state=None):
    payload = {'response_type': 'code', 'client_id': self._client_id,
        'redirect_uri': self._redirect_uri}
    if state is not None:
        payload['state'] = state
    return '%s?%s' % (settings.API_AUTHORIZATION_URL, urllib.urlencode(payload)
        )