def parse_value(self, value_string: str):
    self.value = Decimal(value_string)
    return self.value