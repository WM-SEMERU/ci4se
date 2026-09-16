def mutation_jwt_refresh_token_required(fn):

    @wraps(fn)
    def wrapper(cls, *args, **kwargs):
        token = kwargs.pop(current_app.config[
            'JWT_REFRESH_TOKEN_ARGUMENT_NAME'])
        try:
            verify_refresh_jwt_in_argument(token)
        except Exception as e:
            return cls(AuthInfoField(message=str(e)))
        return fn(*args, **kwargs)
    return wrapper