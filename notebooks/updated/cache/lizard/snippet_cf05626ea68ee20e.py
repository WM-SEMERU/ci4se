def _request(self, method, url, headers=None, params=None, **aio_kwargs):
    auth = None
    access_token = params.pop(self.access_token_key, None)
    if access_token:
        headers['Authorization'] = 'Bearer %s' % access_token
    else:
        auth = BasicAuth(self.client_id, self.client_secret)
    return super(Bitbucket2Client, self)._request(method, url, headers=
        headers, params=params, auth=auth, **aio_kwargs)