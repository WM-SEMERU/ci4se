async def spawn(self, agent_cls, *args, addr=None, **kwargs):
    if addr is None:
        addr = await self._get_smallest_env()
    r_manager = await self.env.connect(addr)
    return await r_manager.spawn(agent_cls, *args, **kwargs)