def call_from_executor(self, callback, _max_postpone_until=None):
    self._calls_from_executor.append(callback)
    windll.kernel32.SetEvent(self._event)