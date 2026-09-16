def update(self, **kwargs):
    url = '/me'
    result = self._put(url, data=kwargs)
    return UserModel.parse(result)