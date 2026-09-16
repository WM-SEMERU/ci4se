def update_token(self):
    logger.info('updating token')
    if None in self.credentials.values():
        raise RuntimeError('You must provide an username and a password')
    credentials = dict(auth=self.credentials)
    url = self.test_url if self.test else self.url
    response = requests.post(url + 'auth', json=credentials)
    data = response.json()['response']
    if 'error_id' in data and data['error_id'] == 'NOAUTH':
        raise BadCredentials()
    if 'error_code' in data and data['error_code'] == 'RATE_EXCEEDED':
        time.sleep(150)
        return
    if 'error_code' in data or 'error_id' in data:
        raise AppNexusException(response)
    self.token = data['token']
    self.save_token()
    return self.token