def get_logged_in_by(self, login, parent_zc, duration=0):
    domain_name = zobjects.Account(name=login).get_domain()
    preauth_key = parent_zc.get_domain(domain_name)['zimbraPreAuthKey']
    rc = self.REST_PREAUTH(self._server_host, parent_zc._server_port,
        preauth_key=preauth_key)
    authToken = rc.get_preauth_token(login)
    self.login_with_authToken(authToken)