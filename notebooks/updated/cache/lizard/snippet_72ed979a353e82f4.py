def add_values(self, values):
    if self.child.is_alive():
        self.parent_pipe.send(values)