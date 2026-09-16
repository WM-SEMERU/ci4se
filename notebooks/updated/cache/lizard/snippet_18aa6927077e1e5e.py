def add_attribute(self, tag, name, value):
    self.add_tag(tag)
    d = self._tags[tag]
    d[name] = value