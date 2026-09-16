def set_default(self, value):
    if value is None:
        self.__default = value
    elif not isinstance(value, str):
        raise TypeError('Default must be set to a String')
    else:
        self.__default = value