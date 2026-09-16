def wrap(self, wrapper):
    if self._recv_thread and self._send_thread:
        self._recv_lock.acquire()
        self._send_lock.acquire()
    self._sock = wrapper(self._sock)
    if self._recv_thread and self._send_thread:
        self._send_lock.release()
        self._recv_lock.release()