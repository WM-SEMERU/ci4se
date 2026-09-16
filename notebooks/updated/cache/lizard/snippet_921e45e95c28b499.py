def add_space(self, line):
    if not isinstance(self.last_item, Space):
        space = Space(self._structure)
        self._structure.append(space)
    self.last_item.add_line(line)
    return self