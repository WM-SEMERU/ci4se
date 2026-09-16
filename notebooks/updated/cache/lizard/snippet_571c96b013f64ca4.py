def _send(self, message):
    params = {'EsendexUsername': self.get_username(), 'EsendexPassword':
        self.get_password(), 'EsendexAccount': self.get_account(),
        'EsendexOriginator': message.from_phone, 'EsendexRecipient': ','.
        join(message.to), 'EsendexBody': message.body, 'EsendexPlainText': '1'}
    if ESENDEX_SANDBOX:
        params['EsendexTest'] = '1'
    response = requests.post(ESENDEX_API_URL, params)
    if response.status_code != 200:
        if not self.fail_silently:
            raise Exception('Bad status code')
        else:
            return False
    if not response.content.startswith(b'Result'):
        if not self.fail_silently:
            raise Exception('Bad result')
        else:
            return False
    response = self._parse_response(response.content.decode('utf8'))
    if ESENDEX_SANDBOX and response['Result'] == 'Test':
        return True
    elif response['Result'].startswith('OK'):
        return True
    elif not self.fail_silently:
        raise Exception('Bad result')
    return False