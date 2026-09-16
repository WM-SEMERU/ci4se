def process_forever(self, timeout=0.2):
    log.debug('process_forever(timeout=%s)', timeout)
    self._looping.set()
    while self._looping.is_set():
        self.process_once(timeout)