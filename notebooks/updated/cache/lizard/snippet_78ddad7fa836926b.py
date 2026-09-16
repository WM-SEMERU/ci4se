def decorate_function(self, name, decorator):
    self.functions[name] = decorator(self.functions[name])