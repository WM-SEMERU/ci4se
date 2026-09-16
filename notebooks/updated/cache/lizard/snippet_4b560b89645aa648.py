def replace(self, p_todos):
    self.erase()
    self.add_todos(p_todos)
    self.dirty = True