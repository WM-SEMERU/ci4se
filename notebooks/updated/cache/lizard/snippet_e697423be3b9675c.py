def recv(self, timeout=None):
    try:
        return self.rx_queue.get(timeout is None or timeout > 0, timeout)
    except queue.Empty:
        return None