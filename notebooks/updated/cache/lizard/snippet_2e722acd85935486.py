def authenticate(self, username=None, password=None, **kwargs):
    if username is None:
        UserModel = get_user_model()
        username = kwargs.get(UserModel.USERNAME_FIELD)
    account = self._stormpath_authenticate(username, password)
    if account is None:
        return None
    return self._create_or_get_user(account)