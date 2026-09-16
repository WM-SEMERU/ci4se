def start(self):
    LOGGER.debug('rest.Driver.start')
    self.session = requests.Session()
    self.session.auth = self.user, self.password