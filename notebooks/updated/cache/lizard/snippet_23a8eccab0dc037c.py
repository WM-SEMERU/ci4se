def require_login_allowed(f):

    @functools.wraps(f)
    def deco(*a, **kw):
        if not __options__.get('allow_login'):
            abort(403, "Login not allowed. Contact admin if it's a mistake")
        return f(*a, **kw)
    return deco