def events(self):
    if not self.event_reflector:
        return []
    events = []
    for event in self.event_reflector.events:
        if event.involved_object.name != self.pod_name:
            continue
        if self._last_event and event.metadata.uid == self._last_event:
            events = []
        else:
            events.append(event)
    return events