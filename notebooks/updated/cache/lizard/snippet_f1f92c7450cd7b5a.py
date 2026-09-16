def delete(self, password, message=''):
    data = {'user': self.user.name, 'passwd': password, 'delete_message':
        message, 'confirm': True}
    return self.request_json(self.config['delete_redditor'], data=data)