def sms_login(self, client_id, phone_number, code, scope='openid'):
    return self.post('https://{}/oauth/ro'.format(self.domain), data={
        'client_id': client_id, 'connection': 'sms', 'grant_type':
        'password', 'username': phone_number, 'password': code, 'scope':
        scope}, headers={'Content-Type': 'application/json'})