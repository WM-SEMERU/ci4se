def change_password(self, client_id, email, connection, password=None):
    return self.post('https://{}/dbconnections/change_password'.format(self
        .domain), data={'client_id': client_id, 'email': email, 'password':
        password, 'connection': connection}, headers={'Content-Type':
        'application/json'})