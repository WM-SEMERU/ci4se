def result(self):
    if self._result.lower() == 'w':
        return WIN
    if self._result.lower() == 'l' and self.overtime != 0:
        return OVERTIME_LOSS
    return LOSS