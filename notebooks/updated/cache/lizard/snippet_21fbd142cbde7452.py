def Instance(expected, message='Not an instance of {}'):

    @wraps(Instance)
    def built(value):
        if not isinstance(value, expected):
            raise Error(message.format(expected.__name__))
        return value
    return built