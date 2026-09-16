def authorized(self):
    if self.redirect_url:
        next_url = self.redirect_url
    elif self.redirect_to:
        next_url = url_for(self.redirect_to)
    else:
        next_url = '/'
    try:
        self.session.parse_authorization_response(request.url)
    except TokenMissing as err:
        message = err.args[0]
        response = getattr(err, 'response', None)
        log.warning('OAuth 1 access token error: %s', message)
        oauth_error.send(self, message=message, response=response)
        return redirect(next_url)
    try:
        token = self.session.fetch_access_token(self.access_token_url,
            should_load_token=False)
    except ValueError as err:
        message = err.args[0]
        response = getattr(err, 'response', None)
        log.warning('OAuth 1 access token error: %s', message)
        oauth_error.send(self, message=message, response=response)
        return redirect(next_url)
    results = oauth_authorized.send(self, token=token) or []
    set_token = True
    for func, ret in results:
        if isinstance(ret, (Response, current_app.response_class)):
            return ret
        if ret == False:
            set_token = False
    if set_token:
        self.token = token
    return redirect(next_url)