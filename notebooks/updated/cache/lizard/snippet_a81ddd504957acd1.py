def get_user_permissions(self, username):
    path = Client.urls['user_permissions'] % (username,)
    conns = self._call(path, 'GET')
    return conns