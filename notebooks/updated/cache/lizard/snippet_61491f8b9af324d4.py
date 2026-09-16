def send(self, message):
    dest = message.headers.get('destination')
    if not dest:
        raise ValueError('Cannot send frame with no destination: %s' % message)
    message.cmd = 'message'
    message.headers.setdefault('message-id', str(uuid.uuid4()))
    bad_subscribers = set()
    for subscriber in self._topics[dest]:
        try:
            subscriber.send_frame(message)
        except:
            self.log.exception(
                'Error delivering message to subscriber %s; client will be disconnected.'
                 % subscriber)
            bad_subscribers.add(subscriber)
    for subscriber in bad_subscribers:
        self.disconnect(subscriber)