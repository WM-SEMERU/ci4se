def authenticate_credentials(self, userid, password, request=None):
    user = auth.authenticate(username=userid, password=password)
    if user is None or user and not user.is_active:
        raise exceptions.AuthenticationFailed('Invalid username/password.')
    return user, None