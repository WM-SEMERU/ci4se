def oauth_generator(function, *args, **kwargs):
    if getattr(args[0], '_use_oauth', False):
        kwargs['_use_oauth'] = True
    return function(*args, **kwargs)