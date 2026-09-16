def get_display_name(self, role):
    if role not in self.flatten:
        raise MissingRole(role)
    return self.flatten[role]['display_name']