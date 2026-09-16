def _wrap_response(self, start, length):
    if self.status_code == 206:
        self.response = _RangeWrapper(self.response, start, length)