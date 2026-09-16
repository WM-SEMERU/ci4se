def get_value(self, index=None):
    if self.value is None:
        return self.default
    if index is not None:
        if self.value[index] is None:
            return self.default
        else:
            value = self.value[index]
    else:
        value = self.value
    return value