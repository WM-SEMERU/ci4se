def settings_module_update(self, mode_audiopin_enable=None,
    mode_audiopass_enable=None, mode_default=None):
    body = {'auth_password': self._password}
    if mode_audiopin_enable:
        body['mode_audiopin_enable'] = mode_audiopin_enable
    if mode_audiopass_enable:
        body['mode_audiopass_enable'] = mode_audiopass_enable
    if mode_default:
        body['mode_default'] = mode_default
    response = self._put(url.settings_modules, body=body)
    self._check_response(response, 200)