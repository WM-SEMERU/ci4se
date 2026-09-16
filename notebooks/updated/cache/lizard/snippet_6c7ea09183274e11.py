def required_permission(f, level):

    @functools.wraps(f)
    def wrapper(request, pid, *args, **kwargs):
        d1_gmn.app.auth.assert_allowed(request, level, pid)
        return f(request, pid, *args, **kwargs)
    return wrapper