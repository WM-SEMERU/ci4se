def custom_callback(self, view_func):

    @wraps(view_func)
    def decorated(*args, **kwargs):
        plainreturn, data = self._process_callback('custom')
        if plainreturn:
            return data
        else:
            return view_func(data, *args, **kwargs)
    self._custom_callback = decorated
    return decorated