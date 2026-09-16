def get_profile_data(self, auth_response):
    res = auth_response
    token = res.get('access_token')
    expires = res.get('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=int(expires))
    session[self.session_key] = token, expires
    me = oauth.facebook.get('me?fields=email,name')
    if me.status != 200:
        return None
    me = me.data
    email = me.get('email')
    id = me.get('id')
    if not id:
        raise x.UserException('Facebook must return a user id')
    data = dict(provider=self.provider, email=email, id=id, token=token,
        expires=expires)
    return data