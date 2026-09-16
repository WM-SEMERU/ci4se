def process(self, username, password, remember=True):
    self.log.debug('Processing login request')
    self.browser.open(self.LOGIN_URL)
    self.log.info('Login page loaded: %s', self.browser.title())
    self.browser.select_form(nr=0)
    self.log.debug('Username: %s', username)
    self.log.debug('Password: %s', password[0] + '*' * (len(password) - 2) +
        password[-1])
    self.log.debug('Remember: %s', remember)
    self.browser.form[self.USERNAME_FIELD] = username
    self.browser.form[self.PASSWORD_FIELD] = password
    self.browser.find_control(self.REMEMBER_FIELD).items[0].selected = remember
    self.browser.submit()
    self.log.debug('Response code: %s', self.browser.response().code)
    self.log.debug('== Cookies ==')
    for cookie in self.cookiejar:
        self.log.debug(cookie)
        self.cookies[cookie.name] = cookie.value
    self.log.debug('== End Cookies ==')
    if self.LOGIN_COOKIE not in self.cookies:
        raise BadLoginException(
            'No login cookie returned, this probably means an invalid login was provided'
            )
    if remember:
        self.log.info('Saving login session to disk')
        self.cookiejar.save()
    self.log.info('Login request successful')
    return self.cookiejar