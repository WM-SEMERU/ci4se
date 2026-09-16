async def send(self, data):
    self.writer.write(data)
    await self.writer.drain()