def get_events(self, *args, **kwargs):
    from .event import Event, EventDataWrapper
    return self.get_related_resource(Event, EventDataWrapper, args, kwargs)