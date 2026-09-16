def is_superuser(self):
    admin_roles = utils.get_admin_roles()
    user_roles = {role['name'].lower() for role in self.roles}
    return not admin_roles.isdisjoint(user_roles)