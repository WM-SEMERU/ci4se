def read_for_stream(self, stream_transport, timeout_ms=None):
    timeout = timeouts.PolledTimeout.from_millis(timeout_ms)
    while not timeout.has_expired(
        ) and stream_transport.local_id in self._stream_transport_map:
        try:
            return stream_transport.message_queue.get(True, 0.01)
        except queue.Empty:
            pass
        if not self._reader_lock.acquire(False):
            continue
        try:
            try:
                return stream_transport.message_queue.get_nowait()
            except queue.Empty:
                pass
            while not timeout.has_expired():
                msg = self._handle_message_for_stream(stream_transport,
                    self.transport.read_message(timeout), timeout)
                if msg:
                    return msg
        finally:
            self._reader_lock.release()
    if timeout.has_expired():
        raise usb_exceptions.AdbTimeoutError('Read timed out for %s',
            stream_transport)
    try:
        return stream_transport.message_queue.get_nowait()
    except queue.Empty:
        raise usb_exceptions.AdbStreamClosedError(
            'Attempt to read from closed or unknown %s', stream_transport)