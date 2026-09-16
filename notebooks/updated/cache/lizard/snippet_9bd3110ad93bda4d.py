def default_intent(self, f):
    self._default_intent_view_func = f

    @wraps(f)
    def wrapper(*args, **kw):
        self._flask_view_func(*args, **kw)
    return f