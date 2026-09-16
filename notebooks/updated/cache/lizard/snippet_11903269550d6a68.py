def __parseParameters(self):
    self.__parameters = []
    for parameter in self.__data['parameters']:
        self.__parameters.append(Parameter(parameter))