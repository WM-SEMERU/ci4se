def user_create(self, email, username, restricted=True):
    params = {'email': email, 'username': username, 'restricted': restricted}
    result = self.client.post('/account/users', data=params)
    if not 'email' and 'restricted' and 'username' in result:
        raise UnexpectedResponseError('Unexpected response when creating user!'
            , json=result)
    u = User(self.client, result['username'], result)
    return u