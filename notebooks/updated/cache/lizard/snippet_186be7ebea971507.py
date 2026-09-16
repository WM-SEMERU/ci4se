def SetCredentials(self, password=None, username=None):
    if password:
        self._password = password
    if username:
        self._user = username