def not26(func):

    @wraps(func)
    def errfunc(*args, **kwargs):
        raise NotImplementedError
    if hexversion < 34013184:
        return errfunc
    else:
        return func