def set_value(self, value: datetime):
    assert isinstance(value, datetime)
    self.value = value