def _get_connection(self):
    kwargs = {'username': self.account, 'api_key': self.secret_key}
    if self.servicenet:
        kwargs['servicenet'] = True
    if self.authurl:
        kwargs['authurl'] = self.authurl
    return cloudfiles.get_connection(**kwargs)