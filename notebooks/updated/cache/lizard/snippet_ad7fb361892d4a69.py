def call_only_once(func):

    def new_func(*args, **kwargs):
        if not new_func._called:
            new_func._called = True
            return func(*args, **kwargs)
    new_func._called = False
    return new_func