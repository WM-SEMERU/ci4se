def save(self):
    self.stack.append(self.dispatch_table)
    self.dispatch_table = self.default_table.copy()