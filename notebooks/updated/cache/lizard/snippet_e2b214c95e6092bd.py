def get_bounce(bounce_id, api_key=None, secure=None, test=None, **request_args
    ):
    return _default_bounce.get(bounce_id, api_key=api_key, secure=secure,
        test=test, **request_args)