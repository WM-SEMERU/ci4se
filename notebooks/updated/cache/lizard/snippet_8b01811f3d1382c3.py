def get_users(self, omit_empty_organisms=False):
    payload = {}
    if omit_empty_organisms:
        payload['omitEmptyOrganisms'] = omit_empty_organisms
    res = self.post('loadUsers', payload)
    data = [_fix_user(user) for user in res]
    return data