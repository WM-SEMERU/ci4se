def yield_sorted_by_type(*typelist):

    def decorate(fun):

        @wraps(fun)
        def decorated(*args, **kwds):
            return iterate_by_type(fun(*args, **kwds), typelist)
        return decorated
    return decorate