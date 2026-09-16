def contribute_to_class(self, process, fields, name):
    self.name = name
    self.process = process
    fields[name] = self