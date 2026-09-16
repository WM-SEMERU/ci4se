def _packet_manager(self):
    while True:
        if self._packets:
            with self._packet_lock:
                now = time.time()
                self._packets[:] = [packet for packet in self._packets if
                    self._packet_timeout(packet, now)]
        time.sleep(ACK_RESEND / 2)