def subscribe(self, event, handler):
    self._handlers.sync_handlers[event].append(handler)