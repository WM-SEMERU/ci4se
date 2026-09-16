async def iter_all(self, direction: msg.StreamDirection=msg.StreamDirection
    .Forward, from_position: Optional[Union[msg.Position, msg.
    _PositionSentinel]]=None, batch_size: int=100, resolve_links: bool=True,
    require_master: bool=False, correlation_id: Optional[uuid.UUID]=None):
    correlation_id = correlation_id
    cmd = convo.IterAllEvents(msg.Position.for_direction(direction,
        from_position), batch_size, resolve_links, require_master,
        direction, self.credential, correlation_id)
    result = await self.dispatcher.start_conversation(cmd)
    iterator = await result
    async for event in iterator:
        yield event