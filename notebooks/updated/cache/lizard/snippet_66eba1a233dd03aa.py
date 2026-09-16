def watch(self, path, action, *args, **kwargs):
    if action is None:
        action = _set_changed
    event_handler = _WatchdogHandler(self, action)
    self._observer.schedule(event_handler, path=path, recursive=True)