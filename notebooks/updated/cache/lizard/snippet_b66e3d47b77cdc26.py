def login(self, username, password, state=None, sync=True):
    auth = APIAuth(self.OAUTH_SCOPES)
    ret = auth.login(username, password, get_mac())
    if ret:
        self.load(auth, state, sync)
    return ret