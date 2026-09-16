def settings_system_update(self, data):
    data['auth_password'] = self._password
    response = self._put(url.settings_system, body=data)
    self._check_response(response, 200)