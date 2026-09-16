def requires_app_credentials(func):

    @wraps(func)
    def auth_wrapper(self, *args, **kwargs):
        client_id, client_secret = self._session.retrieve_client_credentials()
        if client_id and client_secret:
            return func(self, *args, **kwargs)
        else:
            from .models import GitHubError
            r = generate_fake_error_response(
                '{"message": "Requires username/password authentication"}')
            raise GitHubError(r)
    return auth_wrapper