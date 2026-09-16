async def _retrieve_messages_before_strategy(self, retrieve):
    before = self.before.id if self.before else None
    data = await self.logs_from(self.channel.id, retrieve, before=before)
    if len(data):
        if self.limit is not None:
            self.limit -= retrieve
        self.before = Object(id=int(data[-1]['id']))
    return data