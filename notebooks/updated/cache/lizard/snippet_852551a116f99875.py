def authenticate_eauth(self, load):
    if 'eauth' not in load:
        log.warning('Authentication failure of type "eauth" occurred.')
        return False
    if load['eauth'] not in self.opts['external_auth']:
        log.warning('The eauth system "%s" is not enabled', load['eauth'])
        log.warning('Authentication failure of type "eauth" occurred.')
        return False
    if not self.time_auth(load):
        log.warning('Authentication failure of type "eauth" occurred.')
        return False
    return True