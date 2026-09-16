def request_access_token(self, code, redirect_uri=None):
    redirect = redirect_uri or self._redirect_uri
    resp_text = _http('POST', 'https://api.weibo.com/oauth2/access_token',
        client_id=self._client_id, client_secret=self._client_secret,
        redirect_uri=redirect, code=code, grant_type='authorization_code')
    r = _parse_json(resp_text)
    current = int(time.time())
    expires = r.expires_in + current
    remind_in = r.get('remind_in', None)
    if remind_in:
        rtime = int(remind_in) + current
        if rtime < expires:
            expires = rtime
    return JsonDict(access_token=r.access_token, expires=expires, uid=r.get
        ('uid', None))