def remove_by_name(self, name, index=0):
    child = self.child_at_index(name, index)
    self.remove(child)
    return child