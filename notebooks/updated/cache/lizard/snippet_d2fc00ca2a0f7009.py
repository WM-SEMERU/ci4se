def remainder(self, max_value=None):
    if self.value is None:
        return max_value
    remainder = self.value - (time.clock() - self.start)
    if remainder < 0.0:
        return 0.0
    elif max_value is not None and remainder > max_value:
        return max_value
    else:
        return remainder