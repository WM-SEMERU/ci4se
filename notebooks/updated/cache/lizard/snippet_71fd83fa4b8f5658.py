def invite(self, email, roles=None):
    if roles is None:
        role_ids = [self.roles['Guest'].roleId]
    elif roles == 'ALL':
        role_ids = list([i.id for i in self.roles])
    else:
        if 'Guest' not in roles:
            roles.append('Guest')
        role_ids = list([i.id for i in self.roles if i.name in roles])
    self._router.invite_user(data=json.dumps({'organizationId': self.
        organizationId, 'email': email, 'roles': role_ids}))