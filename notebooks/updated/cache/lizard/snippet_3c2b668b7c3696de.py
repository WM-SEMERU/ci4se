def remove_listener(self, event_name, listener):
    self.listeners[event_name].remove(listener)
    return self