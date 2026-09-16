def _reset(self):
    self._socket = None
    self._pending = deque()
    self._out_buffer = ''
    self._buffer = ''
    self._identify_response = {}
    self.last_ready_sent = 0
    self.ready = 0