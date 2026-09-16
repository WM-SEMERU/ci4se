def lazy_result(f):

    @wraps(f)
    def decorated(ctx, param, value):
        return LocalProxy(lambda : f(ctx, param, value))
    return decorated