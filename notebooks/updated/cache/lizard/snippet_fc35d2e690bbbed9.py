def send_request(self, method, url, headers=None, json_data=None, retry=True):
    if not self.cache(CONST.ACCESS_TOKEN) and url != CONST.LOGIN_URL:
        self.login()
    if not headers:
        headers = {}
    if self.cache(CONST.ACCESS_TOKEN):
        headers['Authorization'] = 'Bearer ' + self.cache(CONST.ACCESS_TOKEN)
    headers['user-agent'] = (
        'SkyBell/3.4.1 (iPhone9,2; iOS 11.0; loc=en_US; lang=en-US) com.skybell.doorbell/1'
        )
    headers['content-type'] = 'application/json'
    headers['accepts'] = '*/*'
    headers['x-skybell-app-id'] = self.cache(CONST.APP_ID)
    headers['x-skybell-client-id'] = self.cache(CONST.CLIENT_ID)
    _LOGGER.debug('HTTP %s %s Request with headers: %s', method, url, headers)
    try:
        response = getattr(self._session, method)(url, headers=headers,
            json=json_data)
        _LOGGER.debug('%s %s', response, response.text)
        if response and response.status_code < 400:
            return response
    except RequestException as exc:
        _LOGGER.warning('Skybell request exception: %s', exc)
    if retry:
        self.login()
        return self.send_request(method, url, headers, json_data, False)
    raise SkybellException(ERROR.REQUEST, 'Retry failed')