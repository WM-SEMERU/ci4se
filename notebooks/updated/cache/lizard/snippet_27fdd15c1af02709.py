def error_and_result(f):

    @wraps(f)
    def error_and_result_decorator(*args, **kwargs):
        return error_and_result_decorator_inner_fn(f, False, *args, **kwargs)
    return error_and_result_decorator