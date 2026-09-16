def avoid_parallel_execution(func):

    def func_wrapper(*args, **kwargs):
        if not getattr(func, 'currently_executing', False):
            func.currently_executing = True
            try:
                return func(*args, **kwargs)
            finally:
                func.currently_executing = False
        else:
            logger.verbose('Avoid parallel execution of function {}'.format
                (func))
    return func_wrapper