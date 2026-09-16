def track_trace(self, name, properties=None, severity=None):
    data = channel.contracts.MessageData()
    data.message = name or NULL_CONSTANT_STRING
    if properties:
        data.properties = properties
    if severity is not None:
        data.severity_level = (channel.contracts.MessageData.
            PYTHON_LOGGING_LEVELS.get(severity))
    self.track(data, self._context)