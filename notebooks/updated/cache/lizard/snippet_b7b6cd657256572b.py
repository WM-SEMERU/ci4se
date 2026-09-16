def get_common_password_hash(self, salt):
    password = self._password
    if password is None:
        raise SRPException(
            'User password should be in context for this scenario.')
    return self.hash(salt, self.hash(self._user, password, joiner=':'))