def content(self, value):
    self._validator.validate_message_dict(value)
    self._content = value