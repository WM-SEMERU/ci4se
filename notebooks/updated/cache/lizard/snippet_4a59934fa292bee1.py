def send(self, data):
    if not self._connected:
        raise ConnectionError('Not connected')
    return self._send_queue.put(data)