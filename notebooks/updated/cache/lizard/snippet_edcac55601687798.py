def publish(self, message):
    if not isinstance(message, types.PubsubMessage):
        message = types.PubsubMessage(**message)
    future = None
    with self._state_lock:
        if not self.will_accept(message):
            return future
        new_size = self._size + message.ByteSize()
        new_count = len(self._messages) + 1
        overflow = (new_size > self.settings.max_bytes or new_count >= self
            ._settings.max_messages)
        if not self._messages or not overflow:
            self._messages.append(message)
            self._size = new_size
            future = futures.Future(completed=threading.Event())
            self._futures.append(future)
    if overflow:
        self.commit()
    return future