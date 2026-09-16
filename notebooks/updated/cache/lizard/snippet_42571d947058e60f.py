def _add_users(self, db, mongo_version):
    if self.x509_extra_user:
        auth_dict = {'name': DEFAULT_SUBJECT, 'roles': self._user_roles(db.
            client)}
        db.add_user(**auth_dict)
        self.kwargs['ssl_certfile'] = DEFAULT_CLIENT_CERT
    secondary_login = {'name': self.login, 'roles': self._user_roles(db.client)
        }
    if self.password:
        secondary_login['password'] = self.password
    if mongo_version >= (3, 7, 2):
        secondary_login['mechanisms'] = ['SCRAM-SHA-1']
    db.add_user(**secondary_login)