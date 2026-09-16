def _get_web_auth_token(self):
    request = _Request(self.network, 'auth.getToken')
    request.sign_it()
    doc = request.execute()
    e = doc.getElementsByTagName('token')[0]
    return e.firstChild.data