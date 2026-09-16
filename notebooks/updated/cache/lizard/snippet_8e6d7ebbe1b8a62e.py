def fun_as_arg(self, x, *args):
    fun = args[0]
    more_args = args[1:] if len(args) > 1 else ()
    return fun(x, *more_args)