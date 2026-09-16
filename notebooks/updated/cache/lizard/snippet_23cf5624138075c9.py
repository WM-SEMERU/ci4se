def change_password(self, username, newpassword, raise_on_error=False):
    response = self._put(self.rest_url + '/user/password', data=json.dumps(
        {'value': newpassword}), params={'username': username})
    if response.ok:
        return True
    if raise_on_error:
        raise RuntimeError(response.json()['message'])
    return False