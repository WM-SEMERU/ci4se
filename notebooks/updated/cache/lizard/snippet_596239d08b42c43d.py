def FirstEventTimestamp(self):
    if self._first_event_timestamp is not None:
        return self._first_event_timestamp
    with self._generator_mutex:
        try:
            event = next(self._generator.Load())
            self._ProcessEvent(event)
            return self._first_event_timestamp
        except StopIteration:
            raise ValueError('No event timestamp could be found')