def _validate_value(self, proposal):
    value = proposal['value']
    if self.base ** self.min > value or self.base ** self.max < value:
        value = min(max(value, self.base ** self.min), self.base ** self.max)
    return value