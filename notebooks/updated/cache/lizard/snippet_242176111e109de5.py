def fire(self, *args, **kwargs):
    if self.eventmanager:
        self.eventmanager.got_event(self.name, *args, **kwargs)
    for handler in self:
        try:
            handler(*args, **kwargs)
        except StopIteration:
            break