def retry_login(self):
    if not self.user or not self.password:
        return self.build_response(status=ERROR, error=
            'please set the user and password')
    retry = 0
    not_done = True
    while not_done:
        if self.is_logged_in():
            return self.build_response(status=SUCCESS)
        else:
            if self.verbose:
                log.debug('login attempt={} max={}'.format(retry, self.
                    max_retries))
            if self.login() == LOGIN_SUCCESS:
                return self.build_response(status=SUCCESS)
            else:
                time.sleep(self.login_retry_wait_time)
        retry += 1
        if retry > self.max_retries:
            return self.build_response(status=ERROR, error=
                'failed logging in user={} retries={}'.format(self.user,
                self.max_retries))
    return self.build_response(status=FAILED, error=
        'user={} not able to login attempts={}'.format(self.user, retry))