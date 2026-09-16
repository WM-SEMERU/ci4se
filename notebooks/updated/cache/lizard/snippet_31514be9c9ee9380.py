def add_listener(self, listener):
    internal_listener = partial(self._call_in_reactor_thread, listener)
    self._internal_listeners[listener] = internal_listener
    return self._client.add_listener(internal_listener)