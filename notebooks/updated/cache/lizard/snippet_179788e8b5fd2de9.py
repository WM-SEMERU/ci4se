def connect(self):
    mongodb_args = {'host': self.host, 'port': self.port, 'username': self.
        _username, 'password': self._password, 'authSource': self.
        _auth_source, 'serverSelectionTimeoutMS': self._connect_timeout}
    if self._auth_mechanism is not None:
        mongodb_args['authMechanism'] = self._auth_mechanism
    self._client = MongoClient(**mongodb_args)
    if self._handle_reconnect:
        self._client = MongoClientProxy(self._client)