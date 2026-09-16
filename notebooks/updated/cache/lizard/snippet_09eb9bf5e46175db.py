def add_special(self, name):
    self.undeclared.discard(name)
    self.declared.add(name)