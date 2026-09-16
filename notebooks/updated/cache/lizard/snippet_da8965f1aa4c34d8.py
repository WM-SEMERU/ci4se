def disable(self):
    self._enabled = False
    for child in self.children:
        if isinstance(child, (Container, Widget)):
            child.disable()