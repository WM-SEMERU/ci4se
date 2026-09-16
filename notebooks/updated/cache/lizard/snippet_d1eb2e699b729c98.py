def unbind(self):
    for variable in self.variables:
        self.__unbind_variable(variable)
    for result in self.results:
        self.__unbind_result(result)