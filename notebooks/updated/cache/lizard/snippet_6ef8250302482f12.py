def push(self, node):
    name = self.lookupname
    if (node, name) in self.path:
        return True
    self.path.add((node, name))
    return False