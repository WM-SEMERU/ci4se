def refresh(self):
    res = gpsoauth.perform_oauth(self._email, self._master_token, self.
        _android_id, service=self._scopes, app='com.google.android.keep',
        client_sig='38918a453d07199354f8b19af05ec6562ced5788')
    if 'Auth' not in res:
        if 'Token' not in res:
            raise exception.LoginException(res.get('Error'))
    self._auth_token = res['Auth']
    return self._auth_token