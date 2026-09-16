def as_dictionary(self):
    values = {'type': self._type, self.SERVICE_ENDPOINT: self._service_endpoint
        }
    if self._consume_endpoint is not None:
        values[self.CONSUME_ENDPOINT] = self._consume_endpoint
    if self._values:
        for name, value in self._values.items():
            if isinstance(value, object) and hasattr(value, 'as_dictionary'):
                value = value.as_dictionary()
            elif isinstance(value, list):
                value = [(v.as_dictionary() if hasattr(v, 'as_dictionary') else
                    v) for v in value]
            values[name] = value
    return values