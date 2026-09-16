def _deserialize(self, value, attr, data):
    if value:
        value = self._format_phone_number(value, attr)
    return super(PhoneNumberField, self)._deserialize(value, attr, data)