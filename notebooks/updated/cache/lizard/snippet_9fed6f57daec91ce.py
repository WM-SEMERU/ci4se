def register_with_password(self, username, password):
    response = self.api.register(auth_body={'type': 'm.login.dummy'}, kind=
        'user', username=username, password=password)
    return self._post_registration(response)