def csrf_protect(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        token = session.get('csrf_token', None)
        if token is None or token != request.environ.get('HTTP_X_CSRFTOKEN'):
            logger.warning('Received invalid csrf token. Aborting')
            abort(403)
        return f(*args, **kwargs)
    return wrapper