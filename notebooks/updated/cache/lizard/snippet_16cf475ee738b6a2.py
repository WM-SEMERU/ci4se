def unbind(self, event, callback):
    if self._events.has_key(event) and len(self._events[event]) > 0:
        for _callback in self._events[event]:
            if _callback == callback:
                self._events[event].remove(callback)
            if len(self._events[event]) == 0:
                del self._events[event]