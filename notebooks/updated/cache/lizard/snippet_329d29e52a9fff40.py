async def _retrieve_messages_after_strategy(self, retrieve):
    after = self.after.id if self.after else None
    data = await self.logs_from(self.channel.id, retrieve, after=after)
    if len(data):
        if self.limit is not None:
            self.limit -= retrieve
        self.after = Object(id=int(data[0]['id']))
    return data