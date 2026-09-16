def register(self):
    user, created = self.Model.create_account(self._json_params)
    if user.api_key is None:
        raise JHTTPBadRequest('Failed to generate ApiKey for user')
    if not created:
        raise JHTTPConflict('Looks like you already have an account.')
    self.request._user = user
    headers = remember(self.request, user.username)
    return JHTTPOk('Registered', headers=headers)