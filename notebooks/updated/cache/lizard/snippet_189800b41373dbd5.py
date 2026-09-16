def put_event(self, data):
    try:
        event = self._factory.create(data)
        self._events.put(event)
    except Full:
        raise GerritError('Unable to add event: queue is full')