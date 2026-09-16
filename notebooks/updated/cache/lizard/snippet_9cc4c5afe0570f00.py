def check(*args, **kwds):

    def wrapper(checkfunc):
        return wraps(checkfunc)(FontBakeryCheck(checkfunc, *args, **kwds))
    return wrapper