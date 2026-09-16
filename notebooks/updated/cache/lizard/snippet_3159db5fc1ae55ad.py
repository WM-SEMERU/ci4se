def inactive_time(self):
    if self._inactive_event.is_set():
        return self.pin_factory.ticks_diff(self.pin_factory.ticks(), self.
            _last_changed)
    else:
        return None