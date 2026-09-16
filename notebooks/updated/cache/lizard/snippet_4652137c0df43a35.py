def once(self, event, f=None):

    def _wrapper(f):

        def g(*args, **kwargs):
            self.remove_listener(event, f)
            return f(*args, **kwargs)
        self._add_event_handler(event, f, g)
        return f
    if f is None:
        return _wrapper
    else:
        return _wrapper(f)