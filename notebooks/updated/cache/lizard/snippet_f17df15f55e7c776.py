def used(self, fieldname):
    if fieldname in self.unused:
        self.unused.remove(fieldname)