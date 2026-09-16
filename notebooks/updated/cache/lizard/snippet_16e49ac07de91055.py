def trigger(self, events, *args, **kwargs):
    if not hasattr(self, '_on_off_events'):
        self._on_off_events = {}
    if not hasattr(self, 'exc_info'):
        self.exc_info = None
    logging.debug('OnOffMixin triggering event(s): %s' % events)
    if isinstance(events, (str, unicode)):
        events = [events]
    for event in events:
        if event in self._on_off_events:
            for callback_obj in self._on_off_events[event]:
                callback_obj['callback'](*args, **kwargs)
                callback_obj['calls'] += 1
                if callback_obj['calls'] == callback_obj['times']:
                    self.off(event, callback_obj['callback'])