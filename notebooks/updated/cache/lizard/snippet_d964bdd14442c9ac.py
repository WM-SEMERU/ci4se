def value(self):
    status_code, error_msg, payload = self.check_error()
    if not self._status_ok(status_code) and not payload:
        raise CloudUnhandledError(
            'Attempted to decode async request which returned an error.',
            reason=error_msg, status=status_code)
    return self.db[self.async_id]['payload']