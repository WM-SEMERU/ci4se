def _busy_wait_ms(self, ms):
    start = time.time()
    delta = ms / 1000.0
    while time.time() - start <= delta:
        pass