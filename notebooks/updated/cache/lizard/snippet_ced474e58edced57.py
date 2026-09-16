def close(self):
    if not self.is_closed():
        self._closing = True
        self.sender.send_Close(0, 'Channel closed by application', 0, 0)
        try:
            yield from self.synchroniser.wait(spec.ChannelCloseOK)
        except AMQPError:
            pass
    elif self._closing:
        log.warn('Called `close` on already closing channel...')