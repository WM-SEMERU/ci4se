def emit_event(self, event):
    with self._lock:
        listeners = list(self._event_listeners)
    for cb in list(self._event_listeners):
        try:
            cb(event)
        except:
            logger.exception('Event callback resulted in unhandled exception')