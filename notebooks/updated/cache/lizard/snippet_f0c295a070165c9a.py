def emit(self, record):
    if record.name.startswith('requests'):
        return
    data, header = self._prepPayload(record)
    try:
        self.session.post(self._getEndpoint(), data=data, headers={
            'content-type': header})
    except Exception:
        self.handleError(record)