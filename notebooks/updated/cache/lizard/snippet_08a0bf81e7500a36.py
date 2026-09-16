def maybe_pause_consumer(self):
    if self.load >= 1.0:
        if self._consumer is not None and not self._consumer.is_paused:
            _LOGGER.debug('Message backlog over load at %.2f, pausing.',
                self.load)
            self._consumer.pause()