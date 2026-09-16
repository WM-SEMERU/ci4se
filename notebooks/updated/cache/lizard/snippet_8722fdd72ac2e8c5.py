def open_channel(self):
    _logger.info('Creating a new channel')
    self._connection.channel(on_open_callback=self.on_channel_open)