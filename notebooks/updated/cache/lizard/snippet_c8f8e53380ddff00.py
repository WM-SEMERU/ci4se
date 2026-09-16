def unregister_event(self, event_name, handler):
    try:
        self._event_handlers[event_name].remove(handler)
    except ValueError:
        pass