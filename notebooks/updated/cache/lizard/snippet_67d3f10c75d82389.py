def gt(self, value):
    self.op = '>'
    self.negate_op = '<='
    self.value = self._value(value)
    return self