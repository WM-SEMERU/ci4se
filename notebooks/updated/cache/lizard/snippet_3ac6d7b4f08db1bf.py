def get(self, tags):
    value = tags.get(self.name, '')
    for name in self.alternate_tags:
        value = value or tags.get(name, '')
    value = value or self.default
    return value