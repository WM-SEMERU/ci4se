def apply(self, mapping):
    self.output.seek(0)
    self.output.truncate(0)
    self.interpreter.string(self.template, locals=mapping)
    return self.output.getvalue()