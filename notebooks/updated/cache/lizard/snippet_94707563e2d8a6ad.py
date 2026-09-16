async def iter(self, stream: str, direction: msg.StreamDirection=msg.
    StreamDirection.Forward, from_event: int=None, batch_size: int=100,
    resolve_links: bool=True, require_master: bool=False, correlation_id:
    uuid.UUID=None):
    correlation_id = correlation_id or uuid.uuid4()
    cmd = convo.IterStreamEvents(stream, from_event, batch_size,
        resolve_links, direction=direction, credentials=self.credential)
    result = await self.dispatcher.start_conversation(cmd)
    iterator = await result
    async for event in iterator:
        yield event