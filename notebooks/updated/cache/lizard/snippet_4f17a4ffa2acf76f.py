def api_token_required(f, *args, **kwargs):
    try:
        if args[0].api_token is None:
            raise AttributeError('Parameter api_token is required.')
    except AttributeError:
        raise AttributeError('Parameter api_token is required.')
    return f(*args, **kwargs)