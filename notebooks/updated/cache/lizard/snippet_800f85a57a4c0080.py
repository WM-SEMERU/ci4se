def aside_for(cls, view_name):

    def _decorator(func):
        if not hasattr(func, '_aside_for'):
            func._aside_for = []
        func._aside_for.append(view_name)
        return func
    return _decorator