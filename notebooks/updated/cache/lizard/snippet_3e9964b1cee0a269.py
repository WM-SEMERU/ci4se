def _parallel_receive_loop(self, seconds_to_wait):
    sleep(seconds_to_wait)
    with self._lock:
        self._number_of_threads_receiving_messages += 1
    try:
        with self._lock:
            if self.state.is_waiting_for_start():
                self.start()
        while True:
            with self.lock:
                if self.state.is_connection_closed():
                    return
                self.receive_message()
    finally:
        with self._lock:
            self._number_of_threads_receiving_messages -= 1