async def publish(self, channel, event, data=None):
    msg = {'event': event, 'channel': channel}
    if data:
        msg['data'] = data
    try:
        await self.pubsub.publish(self.prefixed(channel), msg)
    except ConnectionRefusedError:
        self.connection_error = True
        self.logger.critical(
            '%s cannot publish on "%s" channel - connection error', self,
            channel)
    else:
        self.connection_ok()