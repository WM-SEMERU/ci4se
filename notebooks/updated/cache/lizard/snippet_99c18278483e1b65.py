def track_change(self, tile, property_name, value, formatter=None):
    if not self.tracking:
        return
    if len(self._whitelist) > 0 and (tile, property_name
        ) not in self._whitelist:
        return
    if formatter is None:
        formatter = str
    change = StateChange(monotonic(), tile, property_name, value, formatter
        (value))
    with self._lock:
        self.changes.append(change)