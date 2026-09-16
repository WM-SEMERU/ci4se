def fire_update_event(self, *args, **kwargs):
    for _handler in self._on_update:
        _handler(*args, **kwargs)