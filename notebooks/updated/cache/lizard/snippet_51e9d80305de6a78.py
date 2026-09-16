def add_event(self, name, send_event=True, event_factory=None):
    return self.add_events((name,), send_event=send_event, event_factory=
        event_factory)