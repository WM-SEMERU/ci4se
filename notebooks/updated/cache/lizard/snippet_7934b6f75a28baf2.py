def save_cookie(self, response, key='session', expires=None,
    session_expires=None, max_age=None, path='/', domain=None, secure=None,
    httponly=False, force=False):
    if force or self.should_save:
        data = self.serialize(session_expires or expires)
        response.set_cookie(key, data, expires=expires, max_age=max_age,
            path=path, domain=domain, secure=secure, httponly=httponly)