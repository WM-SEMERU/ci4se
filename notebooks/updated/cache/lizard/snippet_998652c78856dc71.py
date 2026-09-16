def finish(self):
    if self._has_responded:
        raise NSQException('already responded')
    self._has_responded = True
    self.on_finish.send(self)