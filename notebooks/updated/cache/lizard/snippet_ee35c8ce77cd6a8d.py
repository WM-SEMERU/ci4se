def etag(self):
    value = []
    for option in self.options:
        if option.number == defines.OptionRegistry.ETAG.number:
            value.append(option.value)
    return value