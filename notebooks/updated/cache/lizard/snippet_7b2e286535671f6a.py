def validate(self, data):
    autos, errors = [], []
    for s in [self._schema(s, error=self._error, ignore_extra_keys=self.
        _ignore_extra_keys) for s in self._args]:
        try:
            validation = s.validate(data)
            self.match_count += 1
            if self.match_count > 1 and self.only_one:
                break
            return validation
        except SchemaError as _x:
            autos, errors = _x.autos, _x.errors
    raise SchemaError(['%r did not validate %r' % (self, data)] + autos, [
        self._error.format(data) if self._error else None] + errors)