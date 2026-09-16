def send(self, email, body):
    print('Connecting server {0}:{1} with {2}:{3}'.format(self._host, self.
        _port, self._login, self._password))
    print('Sending "{0}" to "{1}"'.format(body, email))