def get_events(self):
    ret = []
    while True:
        event = self.event.get_event(wait=1, full=True)
        if event is None:
            return ret
        ret.append(event)