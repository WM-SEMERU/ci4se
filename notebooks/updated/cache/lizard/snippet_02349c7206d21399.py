def remove_user_from_group(self, username, groupname):
    url = self._options['server'] + '/rest/api/latest/group/user'
    x = {'groupname': groupname, 'username': username}
    self._session.delete(url, params=x)
    return True