def Type(expected, message='Not of type {}'):

    @wraps(Type)
    def built(value):
        if type(value) != expected:
            raise Error(message.format(expected.__name__))
        return value
    return built