def sleep(self, seconds):
    try:
        self.lock()
        time.sleep(seconds)
    except compat.TimeoutException:
        _logger.debug(
            'Connection %r timed out while waiting for lock acquisition.',
            self.container_id)
    finally:
        self.release()