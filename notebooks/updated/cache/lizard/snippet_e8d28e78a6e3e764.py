def value(self):
    result = sum(led.value for led in self)
    if self[0].value < self[-1].value:
        result = -result
    return result / len(self)