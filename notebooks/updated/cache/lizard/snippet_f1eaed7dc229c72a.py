def request_start(self):
    self._queue.put(command_packet(CMD_START_STREAM))
    _LOGGER.info('Requesting stream')
    self._source.run()