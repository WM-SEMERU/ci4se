def create_user(self, data):
    log.info('Create user with %s' % data)
    NewID = self.post('users.json', data).get('id')
    log.info('User has been created with ID %s' % NewID)
    return NewID