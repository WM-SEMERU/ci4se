def requires_basic_auth(func):

    @wraps(func)
    def auth_wrapper(self, *args, **kwargs):
        if hasattr(self, '_session') and self._session.auth:
            return func(self, *args, **kwargs)
        else:
            from .models import GitHubError
            r = generate_fake_error_response(
                '{"message": "Requires username/password authentication"}')
            raise GitHubError(r)
    return auth_wrapper