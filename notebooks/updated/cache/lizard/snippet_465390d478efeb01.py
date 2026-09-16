def get_search_token_from_orcid(self, scope='/read-public'):
    payload = {'client_id': self._key, 'client_secret': self._secret,
        'scope': scope, 'grant_type': 'client_credentials'}
    url = '%s/oauth/token' % self._endpoint
    headers = {'Accept': 'application/json'}
    response = requests.post(url, data=payload, headers=headers, timeout=
        self._timeout)
    response.raise_for_status()
    if self.do_store_raw_response:
        self.raw_response = response
    return response.json()['access_token']