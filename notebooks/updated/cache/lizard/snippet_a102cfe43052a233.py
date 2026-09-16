def update(self, user, name=None, password=None, host=None):
    if not any((name, password, host)):
        raise exc.MissingDBUserParameters(
            'You must supply at least one of the following: new username, new password, or new host specification.'
            )
    if not isinstance(user, CloudDatabaseUser):
        user = self.get(user)
    dct = {}
    if name and name != user.name:
        dct['name'] = name
    if host and host != user.host:
        dct['host'] = host
    if password:
        dct['password'] = password
    if not dct:
        raise exc.DBUpdateUnchanged(
            'You must supply at least one changed value when updating a user.')
    uri = '/%s/%s' % (self.uri_base, user.name)
    body = {'user': dct}
    resp, resp_body = self.api.method_put(uri, body=body)
    return None