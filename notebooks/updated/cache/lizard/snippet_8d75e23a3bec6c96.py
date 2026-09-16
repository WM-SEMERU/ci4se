def tell(self, msg, action, learnas=''):
    action = _check_action(action)
    mode = learnas.upper()
    headers = {'Message-class': '', 'Set': 'local'}
    if action == 'learn':
        if mode == 'SPAM':
            headers['Message-class'] = 'spam'
        elif mode in ['HAM', 'NOTSPAM', 'NOT_SPAM']:
            headers['Message-class'] = 'ham'
        else:
            raise SpamCError('The learnas option is invalid')
    elif action == 'forget':
        del headers['Message-class']
        del headers['Set']
        headers['Remove'] = 'local'
    elif action == 'report':
        headers['Message-class'] = 'spam'
        headers['Set'] = 'local, remote'
    elif action == 'revoke':
        headers['Message-class'] = 'ham'
        headers['Remove'] = 'remote'
    return self.perform('TELL', msg, headers)