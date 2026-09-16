def to_iso8601_string(self):
    string = self._to_string('iso8601')
    if self.tz and self.tz.name == 'UTC':
        string = string.replace('+00:00', 'Z')
    return string