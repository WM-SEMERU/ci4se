def get_session_key(self, username, password_hash):
    params = {'username': username, 'authToken': md5(username + password_hash)}
    request = _Request(self.network, 'auth.getMobileSession', params)
    request.sign_it()
    doc = request.execute()
    return _extract(doc, 'key')