def addNotice(self, data):
    LOGGER.info('Sending addnotice to Polyglot: {}'.format(data))
    message = {'addnotice': data}
    self.send(message)