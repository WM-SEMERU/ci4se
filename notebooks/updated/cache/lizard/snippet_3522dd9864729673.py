def trigger(self, event_name, *args, **kwargs):
    ev = Event(event_name, self)
    ev.trigger(*args, **kwargs)
    return ev