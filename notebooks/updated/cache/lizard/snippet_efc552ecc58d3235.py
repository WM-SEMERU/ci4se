def reconnect(self):
    state_change_event = self.handler.event_object()

    def listener(state):
        if state is KazooState.SUSPENDED:
            state_change_event.set()
    self.add_listener(listener)
    self._connection._socket.shutdown(socket.SHUT_RDWR)
    state_change_event.wait(1)
    if not state_change_event.is_set():
        return False
    while not self.connected:
        time.sleep(0.1)
    return True