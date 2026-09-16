def error_handler(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except OAuth2Error as e:
            if hasattr(e, 'redirect_uri'):
                return redirect(e.in_uri(e.redirect_uri))
            else:
                return redirect(e.in_uri(oauth2.error_uri))
    return decorated