def create_user(self, **kwargs):
    roles = kwargs.pop('roles', [])
    user = self.user_model(**self._prepare_create_user_args(**kwargs))
    user = self.put(user)
    for role in roles:
        self.add_role_to_user(user, role)
    self.put(user)
    return user