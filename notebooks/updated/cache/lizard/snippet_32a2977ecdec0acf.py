def from_env(cls):
    token = getenv(cls.TOKEN_ENV_VAR)
    if token is None:
        msg = 'missing environment variable: {!r}'.format(cls.TOKEN_ENV_VAR)
        raise ValueError(msg)
    return cls(api_token=token)