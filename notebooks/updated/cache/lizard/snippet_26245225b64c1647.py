async def _trigger_event(self, event, namespace, *args):
    if namespace in self.handlers and event in self.handlers[namespace]:
        if asyncio.iscoroutinefunction(self.handlers[namespace][event]
            ) is True:
            try:
                ret = await self.handlers[namespace][event](*args)
            except asyncio.CancelledError:
                ret = None
        else:
            ret = self.handlers[namespace][event](*args)
        return ret
    elif namespace in self.namespace_handlers:
        return await self.namespace_handlers[namespace].trigger_event(event,
            *args)