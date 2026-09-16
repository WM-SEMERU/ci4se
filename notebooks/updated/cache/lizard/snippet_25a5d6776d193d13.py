def wait(self, timeout=None):
    flag = self._finished.wait(timeout=timeout)
    if flag is False:
        raise TimeoutExpiredError(
            'Timeout waiting for response to event loop operation')
    if self._exception is not None:
        self._raise_exception()
    return self._result