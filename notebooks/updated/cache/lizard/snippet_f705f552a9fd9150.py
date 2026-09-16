def get_nested_group_users(self, groupname):
    response = self._get(self.rest_url + '/group/user/nested', params={
        'groupname': groupname, 'start-index': 0, 'max-results': 99999})
    if not response.ok:
        return None
    return [u['name'] for u in response.json()['users']]