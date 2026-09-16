def throw(self, type, value=None, traceback=None):
    return self.__wrapped__.throw(type, value, traceback)