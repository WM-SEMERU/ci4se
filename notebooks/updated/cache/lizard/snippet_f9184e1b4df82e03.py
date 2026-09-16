def closest(self):
    current = self.tag
    closest = None
    while closest is None and current is not None:
        if self.match(current):
            closest = current
        else:
            current = self.get_parent(current)
    return closest