def _getPayload(self, record):
    payload = super(LogglyHandler, self)._getPayload(record)
    payload['tags'] = self._implodeTags()
    return payload