def maybe_transactional(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        commit = kwargs.get('commit', True)
        with transaction(commit=commit):
            return func(*args, **kwargs)
    return wrapper