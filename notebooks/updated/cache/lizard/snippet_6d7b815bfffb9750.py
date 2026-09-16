def add_independent_variable(self, variable):
    assert isinstance(variable, IndependentVariable
        ), 'Variable must be an instance of IndependentVariable'
    if self._has_child(variable.name):
        self._remove_child(variable.name)
    self._add_child(variable)
    self._independent_variables[variable.name] = variable