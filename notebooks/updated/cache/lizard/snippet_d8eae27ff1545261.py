def require_login(self, view_func):

    @wraps(view_func)
    def decorated(*args, **kwargs):
        if g.oidc_id_token is None:
            return self.redirect_to_auth_server(request.url)
        return view_func(*args, **kwargs)
    return decorated