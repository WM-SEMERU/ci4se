def extract(self, format, carrier):
    if format in Tracer._supported_formats:
        return self._noop_span_context
    raise UnsupportedFormatException(format)