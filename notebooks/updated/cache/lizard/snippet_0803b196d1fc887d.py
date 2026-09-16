def token(self):
    if AUTH_TOKEN_HEADER in self.request.headers:
        return self.request.headers[AUTH_TOKEN_HEADER]
    else:
        return self.get_cookie(AUTH_COOKIE_NAME)