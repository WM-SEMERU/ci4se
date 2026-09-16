def add(self, event, message=None):

    def decorator(func):
        if isinstance(message, (list, tuple)):
            for it in message:
                self.__add_handler(func, event, message=it)
        else:
            self.__add_handler(func, event, message=message)
        return func
    return decorator