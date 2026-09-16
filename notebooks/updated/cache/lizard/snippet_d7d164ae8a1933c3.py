def _correct_args(func, kwargs):
    args = inspect.getargspec(func)[0]
    return [kwargs[arg] for arg in args] + kwargs['__args']