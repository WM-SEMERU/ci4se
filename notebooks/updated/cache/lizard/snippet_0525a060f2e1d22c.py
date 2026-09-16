def add_subscriber(self, subscriber, precedence=0):
    if not callable(subscriber):
        raise TypeError('Subscriber must be a callable.')
    self._subscribers.append((precedence, subscriber))