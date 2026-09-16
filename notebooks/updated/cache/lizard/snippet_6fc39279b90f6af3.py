def is_instance(self, model):
    result = isinstance(model, self.__model__)
    if result is True:
        return True
    err = 'Object {} is not of type {}'
    raise ValueError(err.format(model, self.__model__))