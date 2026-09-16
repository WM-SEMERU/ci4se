def subscribe_async(self, event, handler):
    self._handlers.async_handlers[event].append(handler)