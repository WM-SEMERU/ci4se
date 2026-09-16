def _cleanup(self):
    self._ack_listener = None
    self._nack_listener = None
    self._broker_cancel_cb_map = None
    super(RabbitBasicClass, self)._cleanup()