def login(self, email, password, max_tries=5):
    self.onLoggingIn(email=email)
    if max_tries < 1:
        raise FBchatUserError('Cannot login: max_tries should be at least one')
    if not (email and password):
        raise FBchatUserError('Email and password not set')
    for i in range(1, max_tries + 1):
        login_successful, login_url = self._login(email, password)
        if not login_successful:
            log.warning('Attempt #{} failed{}'.format(i, {True:
                ', retrying'}.get(i < max_tries, '')))
            time.sleep(1)
            continue
        else:
            self.onLoggedIn(email=email)
            break
    else:
        raise FBchatUserError(
            'Login failed. Check email/password. (Failed on url: {})'.
            format(login_url))