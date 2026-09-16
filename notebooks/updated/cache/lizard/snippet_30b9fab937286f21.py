def bind(self, event_name, callback, first=False):
    if event_name not in self.handlers:
        self.handlers[event_name] = []
    if first:
        self.handlers[event_name].insert(0, callback)
    else:
        self.handlers[event_name].append(callback)