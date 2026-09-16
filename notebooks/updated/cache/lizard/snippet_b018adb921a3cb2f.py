def format_field(self, value, format_spec):
    if format_spec:
        spec, arg = format_spec[0], format_spec[1:]
        arg = arg or None
    else:
        spec = arg = None
    return self._format_field(spec, arg, value, self.numeric_locale)