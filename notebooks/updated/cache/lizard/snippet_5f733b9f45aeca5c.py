def _refresh(self):
    new_token = self.authenticate(self._username, self._password)
    self._token = new_token
    logger.info('New API token received: "{}".'.format(new_token))
    return self._token