def pass_context(f):

    def new_func(*args, **kwargs):
        return f(get_current_context(), *args, **kwargs)
    return update_wrapper(new_func, f)