def has_callbacks(self, name):
    r = self.event_listeners.get(name)
    if not r:
        return False
    return len(r) > 0