def bind(self, event, callback):
    if self._events.has_key(event):
        self._events[event].append(callback)
    else:
        self._events[event] = [callback]