def requeue(self):
    if self.acknowledged:
        raise self.MessageStateError(
            'Message already acknowledged with state: %s' % self._state)
    self.backend.requeue(self.delivery_tag)
    self._state = 'REQUEUED'