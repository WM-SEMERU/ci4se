def tick(self):
    self._handle_command_buffer()
    self._client.release()
    self._client.acquire()
    return self._get_full_state()