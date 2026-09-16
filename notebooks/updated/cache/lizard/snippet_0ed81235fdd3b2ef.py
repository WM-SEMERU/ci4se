def add_handler(self, event, handler):
    if event in self.event_handlers:
        raise ValueError("Cannot register handler for '%s' twice." % event)
    self.event_handlers[event] = handler