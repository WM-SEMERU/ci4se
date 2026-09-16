def local_variables(self):
    return list(set(self.variables) - set(self.returns) - set(self.parameters))