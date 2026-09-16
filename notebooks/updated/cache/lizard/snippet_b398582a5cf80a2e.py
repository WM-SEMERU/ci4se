def on_consumer_cancelled(self, method_frame):
    msg = 'Consumer was cancelled remotely, shutting down: {0!r}'
    logger.info(msg.format(method_frame))
    if self._channel:
        self._channel.close()