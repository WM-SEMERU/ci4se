def sleep(self, response=None):
    if response:
        slept = self.sleep_for_retry(response)
        if slept:
            return
    self._sleep_backoff()