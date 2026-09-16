def get_authorization(self, **kwargs):
    if self.authorization is not None:
        return self.authorization
    auth_class = self.get_authorization_class()
    auth_user = self.get_authorization_user()
    auth_kwargs = {'token': self.get_authorization_token(**kwargs)}
    if auth_user and auth_user.is_authenticated():
        auth_kwargs['created_user'] = self.get_authorization_user()
    self.authorization = auth_class.objects.get_by_token_or_404(**auth_kwargs)
    return self.authorization