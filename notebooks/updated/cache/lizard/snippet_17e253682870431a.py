def get_bounces(api_key=None, secure=None, test=None, **request_args):
    return _default_bounces.get(api_key=api_key, secure=secure, test=test,
        **request_args)