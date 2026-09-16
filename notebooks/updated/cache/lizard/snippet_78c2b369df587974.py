def next(self):
    if self._pattern == zmq.REQ and not self._recv_ready:
        self._socket.send(b'next')
        self._recv_ready = True
    try:
        msg = self._socket.recv_multipart(copy=False)
    except zmq.error.Again:
        raise TimeoutError('No data received from {} in the last {} ms'.
            format(self._socket.getsockopt_string(zmq.LAST_ENDPOINT), self.
            _socket.getsockopt(zmq.RCVTIMEO)))
    self._recv_ready = False
    return self._deserialize(msg)