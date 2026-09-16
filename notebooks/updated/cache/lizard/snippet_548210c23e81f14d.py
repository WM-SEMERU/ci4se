def get_user(self, user_id=None, username=None, email=None):
    if user_id:
        uri = '/users/%s' % user_id
    elif username:
        uri = '/users?name=%s' % username
    elif email:
        uri = '/users?email=%s' % email
    else:
        raise ValueError(
            "You must include one of 'user_id', 'username', or 'email' when calling get_user()."
            )
    resp, resp_body = self.method_get(uri)
    if resp.status_code == 404:
        raise exc.NotFound('No such user exists.')
    users = resp_body.get('users', [])
    if users:
        return [User(self, user) for user in users]
    else:
        user = resp_body.get('user', {})
        if user:
            return User(self, user)
        else:
            raise exc.NotFound('No such user exists.')