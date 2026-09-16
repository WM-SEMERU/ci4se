def login(self, username=None, password=None):
    if username is not None:
        self._username = username
    if password is not None:
        self._password = password
    if self._username is None or not isinstance(self._username, str):
        raise SkybellAuthenticationException(ERROR.USERNAME)
    if self._password is None or not isinstance(self._password, str):
        raise SkybellAuthenticationException(ERROR.PASSWORD)
    self.update_cache({CONST.ACCESS_TOKEN: None})
    login_data = {'username': self._username, 'password': self._password,
        'appId': self.cache(CONST.APP_ID), CONST.TOKEN: self.cache(CONST.TOKEN)
        }
    try:
        response = self.send_request('post', CONST.LOGIN_URL, json_data=
            login_data, retry=False)
    except Exception as exc:
        raise SkybellAuthenticationException(ERROR.LOGIN_FAILED, exc)
    _LOGGER.debug('Login Response: %s', response.text)
    response_object = json.loads(response.text)
    self.update_cache({CONST.ACCESS_TOKEN: response_object[CONST.ACCESS_TOKEN]}
        )
    _LOGGER.info('Login successful')
    return True