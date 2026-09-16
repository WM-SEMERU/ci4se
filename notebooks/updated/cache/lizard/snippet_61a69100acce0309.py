def _bind_ldap(self, ldap, con, username, password):
    try:
        if self.auth_ldap_bind_user:
            self._bind_indirect_user(ldap, con)
            user = self._search_ldap(ldap, con, username)
            if user:
                log.debug('LDAP got User {0}'.format(user))
                username = user[0][0]
            else:
                return False
        log.debug('LDAP bind with: {0} {1}'.format(username, 'XXXXXX'))
        if self.auth_ldap_username_format:
            username = self.auth_ldap_username_format % username
        if self.auth_ldap_append_domain:
            username = username + '@' + self.auth_ldap_append_domain
        con.bind_s(username, password)
        log.debug('LDAP bind OK: {0}'.format(username))
        return True
    except ldap.INVALID_CREDENTIALS:
        return False