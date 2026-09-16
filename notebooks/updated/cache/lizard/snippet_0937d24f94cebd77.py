def on(self, event, listener, *user_args):
    self._listeners[event].append(_Listener(callback=listener, user_args=
        user_args))