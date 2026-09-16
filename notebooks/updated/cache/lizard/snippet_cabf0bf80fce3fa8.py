def validate_wrap(self, value):
    if not isinstance(value, self.type):
        self._fail_validation_type(value, self.type)