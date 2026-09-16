def wait_for_disappearance(self, timeout=120):
    start = time.time()
    while self.exists():
        self.poco.sleep_for_polling_interval()
        if time.time() - start > timeout:
            raise PocoTargetTimeout('disappearance', self)