def raise_null_argument(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as ex:
            if any(statement in ex.args[0] for statement in [
                'takes exactly', 'required positional argument']):
                raise NullArgument('Wrong number of arguments provided: ' +
                    str(ex.args[0]))
            else:
                raise
    return wrapper