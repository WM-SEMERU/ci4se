def connection_lost(self, exc):
    if exc:
        self.logger.error('disconnected due to error')
    else:
        self.logger.info('disconnected because of close/abort.')
    if self.disconnect_callback:
        asyncio.ensure_future(self.disconnect_callback(), loop=self.loop)