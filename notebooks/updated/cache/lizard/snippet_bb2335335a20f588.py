def returns(*checkers_args):

    @decorator
    def run_checkers(func, *args, **kwargs):
        ret = func(*args, **kwargs)
        if type(ret) != tuple:
            ret = ret,
        assert len(ret) == len(checkers_args)
        if checkers_args:
            for idx, checker_function in enumerate(checkers_args):
                if callable(checker_function):
                    result = checker_function(ret[idx])
        return ret
    return run_checkers