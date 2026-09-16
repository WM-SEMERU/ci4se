async def load_credentials(self, credentials):
    split = credentials.split(':')
    self.identifier = split[0]
    self.srp.initialize(binascii.unhexlify(split[1]))
    _LOGGER.debug('Loaded AirPlay credentials: %s', credentials)