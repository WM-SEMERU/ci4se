async def listener(self, channel):
    while True:
        message = await self.channel_layer.receive(channel)
        if not message.get('type', None):
            raise ValueError('Worker received message with no type.')
        scope = {'type': 'channel', 'channel': channel}
        instance_queue = self.get_or_create_application_instance(channel, scope
            )
        await instance_queue.put(message)