def add_line(self, logevent):
    key = None
    self.empty = False
    self.groups.setdefault(key, list()).append(logevent)