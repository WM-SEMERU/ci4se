def timezone(self, value):
    self._timezone = value if isinstance(value, datetime.tzinfo) else tz.gettz(
        value)