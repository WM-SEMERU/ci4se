def login_service_description(self):
    label = 'Login to ' + self.name
    if self.auth_type:
        label = label + ' (' + self.auth_type + ')'
    desc = {'@id': self.login_uri, 'profile': self.profile_base + self.
        auth_pattern, 'label': label}
    if self.header:
        desc['header'] = self.header
    if self.description:
        desc['description'] = self.description
    return desc