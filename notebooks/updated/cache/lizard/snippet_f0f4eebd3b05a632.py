def _allocate_channel(self):
    try:
        channel = yield self.channel()
    except pika.exceptions.NoFreeChannels:
        raise NoFreeChannels()
    _std_log.debug('Created AMQP channel id %d', channel.channel_number)
    if self._confirms:
        yield channel.confirm_delivery()
    defer.returnValue(channel)