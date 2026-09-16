def revoke(self, only_access=False):
    if only_access or self.refresh_token is None:
        super(Authorizer, self).revoke()
    else:
        self._authenticator.revoke_token(self.refresh_token, 'refresh_token')
        self._clear_access_token()
        self.refresh_token = None