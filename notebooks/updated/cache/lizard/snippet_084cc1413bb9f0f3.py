def append_scope(self):
    self.stack.current.append(Scope(self.stack.current.current))