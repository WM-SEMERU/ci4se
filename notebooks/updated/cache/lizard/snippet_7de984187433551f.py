def gen(mimetype):

    def streaming(func, *args, **kwargs):

        @wraps(func)
        def _():
            return Response(func(*args, **kwargs), mimetype=mimetype)
        return _
    return streaming