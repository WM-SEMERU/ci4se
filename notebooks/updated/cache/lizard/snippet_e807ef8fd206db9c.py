def GetEnvironmentVariable(self, name):
    name = name.upper()
    return self._environment_variables.get(name, None)