def set_gamma_value(self, value):
    if isinstance(value, float) is False:
        raise TypeError('The type of __gamma_value must be float.')
    self.__gamma_value = value