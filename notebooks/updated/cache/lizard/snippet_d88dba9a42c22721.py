def helper(*commands):

    def decorated_func(f):
        f.__help_targets__ = list(commands)
        return f
    return decorated_func