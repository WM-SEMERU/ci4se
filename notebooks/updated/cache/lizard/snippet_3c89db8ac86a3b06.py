def remove_specification(self, name):
    if name in self.__specs:
        self.__specs.pop(name)