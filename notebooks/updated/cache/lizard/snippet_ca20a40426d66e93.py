async def get_info(self):
    facade = client.ClientFacade.from_connection(self.connection())
    self._info = await facade.ModelInfo()
    log.debug('Got ModelInfo: %s', vars(self.info))
    return self.info