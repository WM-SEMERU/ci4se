def superuser_api_key_required(f):

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        api_key = current_api_key()
        g.api_key = api_key
        utils.jsonify_assert(api_key.superuser, 
            'API key=%r must be a super user' % api_key.id, 403)
        return f(*args, **kwargs)
    return wrapped