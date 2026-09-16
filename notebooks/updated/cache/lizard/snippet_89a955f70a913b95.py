def settings_system_reset(self):
    data = {'auth_password': self._password}
    response = self._delete(url.settings_system, body=data)
    self._check_response(response, 204)