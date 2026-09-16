def login(self, username=None, password=None, section='default'):
    if self.has_logged_in:
        return True
    if username is None or password is None:
        credential = conf.get_credential(section)
        username = credential['username']
        password = credential['password']
    passport = Passport(username, password)
    r = self.http.post(LOGIN_URL, passport.form)
    if r.state is True:
        self.passport = passport
        passport.data = r.content['data']
        self._user_id = r.content['data']['USER_ID']
        return True
    else:
        msg = None
        if 'err_name' in r.content:
            if r.content['err_name'] == 'account':
                msg = 'Account does not exist.'
            elif r.content['err_name'] == 'passwd':
                msg = 'Password is incorrect.'
        raise AuthenticationError(msg)