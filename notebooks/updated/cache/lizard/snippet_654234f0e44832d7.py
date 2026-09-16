def has_value(self):
    try:
        if isinstance(self.__value, Expression):
            return self.__value.has_value
        return True
    except AttributeError:
        return False