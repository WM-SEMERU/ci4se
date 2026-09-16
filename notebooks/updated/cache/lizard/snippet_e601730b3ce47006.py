def register(self, email, full_name, password, **kwargs):
    params = {'email': email, 'full_name': full_name, 'password': password}
    return self._post('register', params, **kwargs)