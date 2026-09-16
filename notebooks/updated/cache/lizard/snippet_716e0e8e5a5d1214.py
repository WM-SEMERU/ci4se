def replace_variable(self, variable):
    name = variable.__name__
    if self.variables.get(name) is not None:
        del self.variables[name]
    self.load_variable(variable, update=False)