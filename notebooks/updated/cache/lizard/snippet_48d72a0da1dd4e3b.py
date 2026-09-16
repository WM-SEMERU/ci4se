def unsuppress(self, email):
    params = {'email': email}
    response = self._put(self.uri_for('unsuppress'), body=' ', params=params)