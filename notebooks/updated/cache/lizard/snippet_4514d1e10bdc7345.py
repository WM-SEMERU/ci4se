def register_monitor(self, devices, events, callback):
    events = list(events)
    devices = list(devices)
    for event in events:
        if event not in self.SUPPORTED_EVENTS:
            raise ArgumentError('Unknown event type {} specified'.format(
                event), events=events)
    monitor_id = str(uuid.uuid4())
    action = monitor_id, 'add', devices, events
    self._callbacks[monitor_id] = callback
    if self._currently_notifying:
        self._deferred_adjustments.append(action)
    else:
        self._adjust_monitor_internal(*action)
    return monitor_id