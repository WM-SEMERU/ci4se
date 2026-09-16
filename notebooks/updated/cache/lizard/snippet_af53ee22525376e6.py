async def rpc_message(self, request, message):
    await self.pubsub.publish(self.channel, message)
    return 'OK'