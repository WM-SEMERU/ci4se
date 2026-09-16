def run(self, cmd):
    cmd = dict(cmd)
    client = 'minion'
    mode = cmd.get('mode', 'async')
    funparts = cmd.get('fun', '').split('.')
    if len(funparts) > 2 and funparts[0] in ['wheel', 'runner']:
        client = funparts[0]
        cmd['fun'] = '.'.join(funparts[1:])
    if not ('token' in cmd or 'eauth' in cmd and 'password' in cmd and 
        'username' in cmd):
        raise EauthAuthenticationError('No authentication credentials given')
    executor = getattr(self, '{0}_{1}'.format(client, mode))
    result = executor(**cmd)
    return result