def username(self, value):
    self._username = value
    self._connectionXML.set('username', value)